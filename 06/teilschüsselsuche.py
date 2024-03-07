# Vorausgesetzt: Funktionen encrypt, s_box_substitution, p_box_permutation aus dem vorherigen Skript
# SPN-Verschlüsselung
import sys, random

def s_box_substitution(input_val):
    s_box = [0xE, 0x4, 0xD, 0x1, 0x2, 0xF, 0xB, 0x8, 0x3, 0xA, 0x6, 0xC, 0x5, 0x9, 0x0, 0x7]
    return s_box[input_val]

def p_box_permutation(input_val):
    p_box = [0, 4, 8, 12, 1, 5, 9, 13, 2, 6, 10, 14, 3, 7, 11, 15]
    output_val = 0
    for bit in range(16):
        output_val |= ((input_val >> bit) & 1) << p_box[bit]
    return output_val

def round_function(block, key):
    # Anwendung der S-Box-Substitution und P-Box-Permutation
    substituted = sum([s_box_substitution((block >> (4*i)) & 0xF) << (4*i) for i in range(4)])
    permuted = p_box_permutation(substituted)
    return permuted ^ key

def encrypt(input_hex, key_hex):
    key = int(key_hex, 16)
    blocks = [input_hex[i:i+4] for i in range(0, len(input_hex), 4)]
    encrypted_blocks = []

    for block_hex in blocks:
        block = int(block_hex, 16)
        for _ in range(4):  # 4 Runden
            block = round_function(block, key)
        encrypted_blocks.append(format(block, '04x'))

    return ''.join(encrypted_blocks)

def generate_pairs(num_pairs, key):
    pairs = []
    for _ in range(num_pairs):
        plaintext = format(random.randint(0, 0xFFFF), '04x')  # Zufälliger 4-Bit-Klartext
        ciphertext = encrypt(plaintext, key)
        pairs.append((plaintext, ciphertext))
    return pairs

def linear_approximation_sbox(input_val):
    # Rückgabe des linearen Approximationswerts für eine S-Box
    # Beispiel: U1 ⊕ U3 ⊕ U4 ⊕ V2 für eine bestimmte S-Box
    output_val = s_box_substitution(input_val)
    return ((input_val >> 0) & 1) ^ ((input_val >> 2) & 1) ^ ((input_val >> 3) & 1) ^ ((output_val >> 1) & 1)

def search_partial_key(pairs):
    max_bias = 0
    best_keys = (0, 0)
    for L1 in range(16):
        for L2 in range(16):
            bias_sum = 0
            for plaintext, ciphertext in pairs:
                plaintext = int(plaintext, 16)
                ciphertext = int(ciphertext, 16)
                u4_2 = linear_approximation_sbox((L1 ^ (ciphertext >> 8)) & 0xF)  # Entschlüsselung des Teils v^4_{(2)}
                u4_4 = linear_approximation_sbox((L2 ^ (ciphertext >> 0)) & 0xF)  # Entschlüsselung des Teils v^4_{(4)}
                if (plaintext >> 4 & 1) ^ (plaintext >> 6 & 1) ^ (plaintext >> 7 & 1) ^ u4_2 ^ u4_4 == 0:
                    bias_sum += 1
            bias = abs(bias_sum - len(pairs) / 2)
            if bias > max_bias:
                max_bias = bias
                best_keys = (L1, L2)
    return best_keys

def read_pairs_from_files(plaintext_file, ciphertext_file):
    """Liest Klartext-Kryptotext-Paare aus Dateien."""
    with open(plaintext_file, 'r') as pt_file, open(ciphertext_file, 'r') as ct_file:
        plaintexts = pt_file.readlines()
        ciphertexts = ct_file.readlines()

    # Entferne Whitespaces und Newlines
    plaintexts = [pt.strip() for pt in plaintexts]
    ciphertexts = [ct.strip() for ct in ciphertexts]

    # Kombiniere zu Paaren
    pairs = list(zip(plaintexts, ciphertexts))
    return pairs

# Hauptprogramm
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python search_partial_key.py [Klartexte] [Kryptotexte]")
        sys.exit(1)

    plaintext_file, ciphertext_file = sys.argv[1], sys.argv[2]

    # Lese Klartext-Kryptotext-Paare aus den Dateien
    pairs = read_pairs_from_files(plaintext_file, ciphertext_file)

    # Führe die Teilschlüsselsuche mit den gelesenen Paaren durch
    best_keys = search_partial_key(pairs)
    print(best_keys)

