# AES Encryption and Decryption in Python

This Python script provides an implementation of the Advanced Encryption Standard (AES) for encryption and decryption of data.

## Functions

The script includes the following functions:

- `sub_bytes(state, sbox)`: Substitutes bytes in the state matrix using the provided substitution box (sbox).
- `shift_rows(state)`: Performs a cyclic shift on the rows of the state matrix.
- `mix_columns(state)`: Mixes the columns of the state matrix.
- `add_round_key(state, key)`: Adds (XORs) the round key to the state matrix.
- `convert_hex_string_to_matrix(hex_string)`: Converts a hexadecimal string to a 4x4 matrix.
- `aes_encrypt(plaintext, keys, sbox)`: Encrypts the plaintext using the provided keys and sbox.
- `inv_sub_bytes(state, inv_sbox)`: Performs the inverse byte substitution on the state matrix using the provided inverse sbox.
- `inv_shift_rows(state)`: Performs the inverse row shifting on the state matrix.
- `inv_mix_columns(state)`: Performs the inverse column mixing on the state matrix.
- `aes_decrypt(ciphertext, keys, inv_sbox)`: Decrypts the ciphertext using the provided keys and inverse sbox.
- `load_sbox_from_file(filename)`: Loads a substitution box from a file.
- `load_key_from_file(filename)`: Loads an encryption key from a file.
- `convert_hex_string_to_byte_array(hex_string)`: Converts a hexadecimal string to a byte array.
- `convert_byte_array_to_hex_string(byte_array)`: Converts a byte array to a hexadecimal string.

## Usage

To use this script, you need to have the plaintext or ciphertext, the keys, and the sbox or inverse sbox. The keys and sboxes can be loaded from files using the provided functions.

Here is an example of how to use the script:

```python
sbox = load_sbox_from_file('SBox.txt')
inv_sbox = load_sbox_from_file('SBoxInvers.txt')
example_key = [load_key_from_file('Beispiel_key.txt')[i:i + 4] for i in range(0, 44, 4)] # Assumes 11 round keys

plaintext_hex = "5c f6 ee 79 2c df 05 e1 ba 2b 63 25 c4 1a 5f 10"
ciphertext_hex = "e2 48 89 ba aa dd 90 6b 06 30 06 59 8b 8c e4 59"

encrypted = aes_encrypt(plaintext_hex, example_key, sbox)
decrypted = aes_decrypt(ciphertext_hex, example_key, inv_sbox)

print("Encrypted:", convert_byte_array_to_hex_string(encrypted))
print("Decrypted:", convert_byte_array_to_hex_string(decrypted))