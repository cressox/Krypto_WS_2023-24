# AES Encryption Modes in Python

This Python script provides an implementation of different modes of operation for the Advanced Encryption Standard (AES) for encryption and decryption of data.

## Functions

The script includes the following functions:

- `aes_encrypt_block(plaintext_block, key)`: Encrypts a plaintext block using the provided key.
- `aes_decrypt_block(ciphertext_block, key)`: Decrypts a ciphertext block using the provided key.
- `pad(plaintext, block_size)`: Adds padding to the plaintext if necessary.
- `unpad(plaintext)`: Removes padding from the plaintext.
- `ecb_encrypt(plaintext, key)`: Encrypts the plaintext using the Electronic Codebook (ECB) mode.
- `xor_bytes(a, b)`: Performs a XOR operation between two byte arrays.
- `ecb_decrypt(ciphertext, key)`: Decrypts the ciphertext using the ECB mode.
- `cbc_encrypt(plaintext, key, iv)`: Encrypts the plaintext using the Cipher Block Chaining (CBC) mode.
- `cbc_decrypt(ciphertext, key, iv)`: Decrypts the ciphertext using the CBC mode.
- `ofb_encrypt_decrypt(plaintext, key, iv)`: Encrypts or decrypts the plaintext using the Output Feedback (OFB) mode.
- `ctr_encrypt_decrypt(plaintext, key, nonce)`: Encrypts or decrypts the plaintext using the Counter (CTR) mode.

## Usage

To use this script, you need to have the plaintext or ciphertext, the key, and for some modes, an initialization vector (iv) or nonce. Here is an example of how to use the script:

```python
key = os.urandom(16)
iv = os.urandom(16)
nonce = os.urandom(8)
plaintext = b"This is a test."

ciphertext_ecb = ecb_encrypt(plaintext, key)
decrypted_ecb = ecb_decrypt(ciphertext_ecb, key)

ciphertext_cbc = cbc_encrypt(plaintext, key, iv)
decrypted_cbc = cbc_decrypt(ciphertext_cbc, key, iv)

ciphertext_ofb = ofb_encrypt_decrypt(plaintext, key, iv)
decrypted_ofb = ofb_encrypt_decrypt(ciphertext_ofb, key, iv)

ciphertext_ctr = ctr_encrypt_decrypt(plaintext, key, nonce)
decrypted_ctr = ctr_encrypt_decrypt(ciphertext_ctr, key, nonce)

print("ECB Decrypted:", decrypted_ecb)
print("CBC Decrypted:", decrypted_cbc)
print("OFB Decrypted:", decrypted_ofb)
print("CTR Decrypted:", decrypted_ctr)