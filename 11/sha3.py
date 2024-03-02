import sys

def pad_message(N, r):
    """Pad the message for SHA-3 with the specified block size `r`."""
    N += "01"  # Add the start of the padding sequence
    while (len(N) * 4) % r != r - 4:
        N += "0"  # Add zeros
    N += "1"  # Finish the padding sequence
    return N

def split_into_blocks(N, r):
    """Split the padded message into blocks of size `r`."""
    block_size = r // 4  # Convert bit size to hex size
    return [N[i:i+block_size] for i in range(0, len(N), block_size)]

def theta(A):
    B = [[[A[x][y][z] for z in range(64)] for y in range(5)] for x in range(5)]
    C = [[0]*64 for _ in range(5)]
    for x in range(5):
        for z in range(64):
            C[x][z] = A[x][0][z] ^ A[x][1][z] ^ A[x][2][z] ^ A[x][3][z] ^ A[x][4][z]
    for x in range(5):
        for y in range(5):
            for z in range(64):
                B[x][y][z] = A[x][y][z] ^ C[(x-1) % 5][z] ^ C[(x+1) % 5][(z-1) % 64]
    return B

def permutation_function(S):
    A = [[[0 for _ in range(64)] for _ in range(5)] for _ in range(5)]
    for i, bit in enumerate(bin(int(S, 16))[2:].zfill(1600)):
        A[i % 5][(i // 5) % 5][i // 25] = int(bit)
    for _ in range(24):
        A = theta(A)
    bits = ''.join(str(A[x][y][z]) for x in range(5) for y in range(5) for z in range(64))
    S = hex(int(bits, 2))[2:].rstrip('L').zfill(1600 // 4)
    return S

def sha3_224(input_file, output_file, r=1152, d=224):
    with open(input_file, 'r') as f:
        N = f.read().strip()
    N_padded = pad_message(N, r)
    blocks = split_into_blocks(N_padded, r)
    S = '0' * (1600 // 4)  # State `S` as a hex string
    for block in blocks:
        block_bin = bin(int(block, 16))[2:].zfill(len(block) * 4)
        S_bin = bin(int(S, 16))[2:].zfill(len(S) * 4)
        S = ''.join(str(int(b) ^ int(s)) for b, s in zip(block_bin, S_bin))
        S = hex(int(S, 2))[2:].rstrip('L').zfill(len(S) // 4)
        S = permutation_function(S)
    hash_value = S[:d // 4]
    with open(output_file, 'w') as f:
        f.write(hex(int(hash_value)))

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <input file> <output file>")
        sys.exit(1)
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    sha3_224(input_file, output_file)
