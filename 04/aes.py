def sub_bytes(state, sbox):
    return [[sbox[byte] for byte in word] for word in state]

def shift_rows(state):
    return [state[row][row:] + state[row][:row] for row in range(4)]

def mix_columns(state):
    def xtime(a):
        return (((a << 1) ^ 0x1B) & 0xFF) if (a & 0x80) else (a << 1)

    def mix_single_column(a):
        t = a[0] ^ a[1] ^ a[2] ^ a[3]
        col = [t ^ xtime(a[i] ^ a[(i + 1) % 4]) for i in range(4)]
        return col

    return [mix_single_column([state[row][col] for row in range(4)]) for col in range(4)]

def add_round_key(state, key):
    return [[byte ^ key[row][col] for col, byte in enumerate(word)] for row, word in enumerate(state)]

def convert_hex_string_to_matrix(hex_string):
    byte_array = [int(hex_val, 16) for hex_val in hex_string.split()]
    return [byte_array[i:i + 4] for i in range(0, len(byte_array), 4)]

def aes_encrypt(plaintext, keys, sbox):
    state = convert_hex_string_to_matrix(plaintext)
    state = add_round_key(state, keys[0])

    for i in range(1, 10):
        state = sub_bytes(state, sbox)
        state = shift_rows(state)
        state = mix_columns(state)
        state = add_round_key(state, keys[i])

    state = sub_bytes(state, sbox)
    state = shift_rows(state)
    state = add_round_key(state, keys[10])

    return [byte for word in state for byte in word]

def inv_sub_bytes(state, inv_sbox):
    return [[inv_sbox[byte] for byte in word] for word in state]

def inv_shift_rows(state):
    return [state[row][-row:] + state[row][:-row] for row in range(4)]

def inv_mix_columns(state):
    def xtime(a):
        return (((a << 1) ^ 0x1B) & 0xFF) if (a & 0x80) else (a << 1)

    def inv_mix_single_column(a):
        u = xtime(xtime(a[0] ^ a[2]))
        v = xtime(xtime(a[1] ^ a[3]))
        col = [a[i] ^ u ^ xtime(a[i] ^ a[(i + 1) % 4]) ^ v for i in range(4)]
        return col

    return [inv_mix_single_column([state[row][col] for row in range(4)]) for col in range(4)]

def aes_decrypt(ciphertext, keys, inv_sbox):
    state = convert_hex_string_to_matrix(ciphertext)
    state = add_round_key(state, keys[10])

    for i in range(9, 0, -1):
        state = inv_shift_rows(state)
        state = inv_sub_bytes(state, inv_sbox)
        state = add_round_key(state, keys[i])
        state = inv_mix_columns(state)

    state = inv_shift_rows(state)
    state = inv_sub_bytes(state, inv_sbox)
    state = add_round_key(state, keys[0])

    return [byte for word in state for byte in word]

def load_sbox_from_file(filename):
    with open(filename, 'r') as file:
        sbox_data = file.read()
        sbox = [int(hex_val, 16) for hex_val in sbox_data.split()]
    return sbox

def load_key_from_file(filename):
    with open(filename, 'r') as file:
        key_data = file.read()
        key = [int(hex_val, 16) for hex_val in key_data.split()]
        # Umwandeln in eine Matrix von 4x4 Bytes
        key_matrix = [key[i:i + 4] for i in range(0, len(key), 4)]
    return key_matrix

def convert_hex_string_to_byte_array(hex_string):
    return [int(hex_val, 16) for hex_val in hex_string.split()]

def convert_byte_array_to_hex_string(byte_array):
    return ' '.join('{:02x}'.format(byte) for byte in byte_array)

if __name__ == "__main__":
    sbox = load_sbox_from_file('SBox.txt')
    inv_sbox = load_sbox_from_file('SBoxInvers.txt')
    example_key = [load_key_from_file('Beispiel_key.txt')[i:i + 4] for i in range(0, 44, 4)] # Annahme: 11 Rundenschlüssel

    plaintext_hex = "5c f6 ee 79 2c df 05 e1 ba 2b 63 25 c4 1a 5f 10"
    ciphertext_hex = "e2 48 89 ba aa dd 90 6b 06 30 06 59 8b 8c e4 59"

    encrypted = aes_encrypt(plaintext_hex, example_key, sbox)
    decrypted = aes_decrypt(ciphertext_hex, example_key, inv_sbox)

    print("Encrypted:", convert_byte_array_to_hex_string(encrypted))
    print("Decrypted:", convert_byte_array_to_hex_string(decrypted))