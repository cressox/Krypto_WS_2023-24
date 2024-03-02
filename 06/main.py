def hex_to_bin(hex_str):
    return bin(int(hex_str, 16))[2:].zfill(16)

def bin_to_hex(bin_str):
    return hex(int(bin_str, 2))[2:].zfill(4)

def substitute(s_box, input_bin):
    return ''.join(s_box[int(input_bin[i:i+4], 2)] for i in range(0, 16, 4))

def permute(p_box, input_bin):
    return ''.join(input_bin[p_box[i]-1] for i in range(16))

def spn_encrypt(plaintext_hex, key_hex):
    s_box = {'0': 'E', '1': '4', '2': 'D', '3': '1', '4': '2', '5': 'F', '6': 'B', '7': '8', '8': '3', '9': 'A', 'A': '6', 'B': 'C', 'C': '5', 'D': '9', 'E': '0', 'F': '7'}
    p_box = {i+1: [1, 5, 9, 13, 2, 6, 10, 14, 3, 7, 11, 15, 4, 8, 12, 16][i] for i in range(16)}
    plaintext_bin = hex_to_bin(plaintext_hex)
    key_bin = hex_to_bin(key_hex)

    for _ in range(4):  # 4 Runden
        plaintext_bin = xor_bytes(plaintext_bin, key_bin)
        plaintext_bin = substitute(s_box, plaintext_bin)
        plaintext_bin = permute(p_box, plaintext_bin)

    ciphertext_bin = xor_bytes(plaintext_bin, key_bin)
    return bin_to_hex(ciphertext_bin)

# XOR-Funktion
def xor_bytes(a, b):
    return ''.join(str(int(x) ^ int(y)) for x, y in zip(a, b))

# Beispielverwendung
plaintext_hex = "1234"  # Beispiel-Plaintext in Hex
key_hex = "1A2B"       # Beispiel-Key in Hex
ciphertext_hex = spn_encrypt(plaintext_hex, key_hex)
print("Ciphertext (Hex):", ciphertext_hex)
