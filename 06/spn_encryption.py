# SPN-Verschlüsselung

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

# Beispielaufruf
if __name__ == "__main__":
    import sys
    if len(sys.argv) != 4:
        print("Usage: python encrypt.py [Input] [Schlüssel] [Output]")
        sys.exit(1)

    input_hex = sys.argv[1]
    key_hex = sys.argv[2]
    output_file = sys.argv[3]

    with open(input_hex, 'r') as f:
        plaintext = f.read()

    with open(key_hex, 'r') as f:
        key = f.read()

    encrypted_text = encrypt(plaintext, key)

    with open(output_file, 'w') as f:
        f.write(encrypted_text)
