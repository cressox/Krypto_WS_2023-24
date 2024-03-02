import sys

# Festlegung der Lookup-Tabelle für die Rho-Transformation
rho_shifts = [
    0,  1, 62, 28, 27,
    36, 44,  6, 55, 20,
     3, 10, 43, 25, 39,
    41, 45, 15, 21,  8,
    18,  2, 61, 56, 14,
]

# Rundenkonstanten für die Iota-Transformation
round_constants = [
    0x0000000000000001, 0x0000000000008082, 0x800000000000808A,
    0x8000000080008000, 0x000000000000808B, 0x0000000080000001,
    0x8000000080008081, 0x8000000000008009, 0x000000000000008A,
    0x0000000000000088, 0x0000000080008009, 0x000000008000000A,
    0x000000008000808B, 0x800000000000008B, 0x8000000000008089,
    0x8000000000008003, 0x8000000000008002, 0x8000000000000080,
    0x000000000000800A, 0x800000008000000A, 0x8000000080008081,
    0x8000000000008080, 0x0000000080000001, 0x8000000080008008,
]
def rho(A):
    B = [[[A[x][y][z] for z in range(64)] for y in range(5)] for x in range(5)]
    for x in range(5):
        for y in range(5):
            shift = rho_shifts[5 * x + y]
            B[x][y] = A[x][y][shift:] + A[x][y][:shift]  # Zyklisches Rotieren
    return B

def pi(A):
    B = [[[0 for z in range(64)] for y in range(5)] for x in range(5)]
    for x in range(5):
        for y in range(5):
            B[x][y] = A[(3*y + x) % 5][x]
    return B

def chi(A):
    B = [[[0 for z in range(64)] for y in range(5)] for x in range(5)]
    for x in range(5):
        for y in range(5):
            for z in range(64):
                B[x][y][z] = A[x][y][z] ^ ((~A[x][(y+1)%5][z]) & A[x][(y+2)%5][z])
    return B

def iota(A, round_index):
    A[0][0] = [int(a) ^ int(b) for a, b in zip(A[0][0], list(format(round_constants[round_index], '064b')))]
    return A

def pad_message(N, r):
    """Pad the message for SHA-3 with the specified block size `r`."""
    N_bin = bin(int(N, 16))[2:].zfill(len(N) * 4)  # Konvertierung von Hex zu Binär
    N_bin += "01"  # Start des Padding
    while len(N_bin) % r != r - 2:
        N_bin += "0"  # Hinzufügen von Nullen
    N_bin += "1"  # Abschluss des Padding
    return N_bin

def split_into_blocks(N_bin, r):
    """Split the padded binary message into blocks of size `r`."""
    return [N_bin[i:i+r] for i in range(0, len(N_bin), r)]

def string_to_state_array(S):
    """Wandelt den Binärstring S in ein 5x5-Array von 64-Bit-Wörtern um."""
    A = [[[0 for _ in range(64)] for _ in range(5)] for _ in range(5)]
    bit_index = 0
    for x in range(5):
        for y in range(5):
            for z in range(64):
                if bit_index < len(S):
                    A[x][y][z] = int(S[bit_index])
                bit_index += 1
    return A

def state_array_to_string(A):
    """Wandelt ein 5x5-Array von 64-Bit-Wörtern zurück in einen Binärstring."""
    S = ''
    for x in range(5):
        for y in range(5):
            for z in range(64):
                S += str(A[x][y][z])
    return S

def sha3_224(input_string):
    r = 1152
    d = 224
    N_bin = pad_message(input_string, r)
    blocks = split_into_blocks(N_bin, r)

    S = '0' * 1600  # Initialisierung des Zustands S in Binär

    for block in blocks:
        S_xor = ''.join(str(int(b) ^ int(s)) for b, s in zip(block, S))
        A = string_to_state_array(S_xor)
        for round_index in range(24):
            A = rho(A)
            A = pi(A)
            A = chi(A)
            A = iota(A, round_index)
        S = state_array_to_string(A)

    hash_bin = S[:d]  # Extraktion der ersten `d` Bits
    hash_hex = hex(int(hash_bin, 2))[2:].zfill(d // 4)
    return hash_hex

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <input file> <output file>")
        sys.exit(1)

    input_file, output_file = sys.argv[1], sys.argv[2]

    with open(input_file, 'r') as f:
        input_string = f.read().strip()

    hash_value = sha3_224(input_string)

    with open(output_file, 'w') as f:
        f.write(hash_value)