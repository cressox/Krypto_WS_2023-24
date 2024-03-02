import os

# Grundlegende AES-Funktionen (vereinfacht)
def aes_encrypt_block(plaintext_block, key):
    # Implementierung der Blockverschlüsselung (AES)
    # Dies ist eine vereinfachte Darstellung. Eine vollständige Implementierung
    # würde alle AES-Schritte einschließen: SubBytes, ShiftRows, MixColumns usw.
    return plaintext_block  # Dummy-Implementierung

def aes_decrypt_block(ciphertext_block, key):
    # Implementierung der Blockentschlüsselung (AES)
    return ciphertext_block  # Dummy-Implementierung

def pad(plaintext, block_size):
    # Padding für den letzten Block, falls erforderlich
    padding_len = block_size - len(plaintext) % block_size
    return plaintext + bytes([padding_len] * padding_len)

def unpad(plaintext):
    # Entfernen des Paddings vom letzten Block
    padding_len = plaintext[-1]
    return plaintext[:-padding_len]

# ECB-Modus
def ecb_encrypt(plaintext, key):
    plaintext = pad(plaintext, 16)
    ciphertext = b''
    for i in range(0, len(plaintext), 16):
        block = plaintext[i:i + 16]
        encrypted_block = aes_encrypt_block(block, key)
        ciphertext += encrypted_block
    return ciphertext

def xor_bytes(a, b):
    """Führt eine XOR-Operation zwischen zwei Byte-Arrays aus."""
    return bytes(x ^ y for x, y in zip(a, b))

def ecb_decrypt(ciphertext, key):
    plaintext = b''
    for i in range(0, len(ciphertext), 16):
        block = ciphertext[i:i + 16]
        decrypted_block = aes_decrypt_block(block, key)
        plaintext += decrypted_block
    return unpad(plaintext)

# CBC-Modus
def cbc_encrypt(plaintext, key, iv):
    plaintext = pad(plaintext, 16)
    ciphertext = b''
    previous_block = iv
    for i in range(0, len(plaintext), 16):
        block = xor_bytes(plaintext[i:i + 16], previous_block)
        encrypted_block = aes_encrypt_block(block, key)
        ciphertext += encrypted_block
        previous_block = encrypted_block
    return ciphertext

def cbc_decrypt(ciphertext, key, iv):
    plaintext = b''
    previous_block = iv
    for i in range(0, len(ciphertext), 16):
        block = ciphertext[i:i + 16]
        decrypted_block = aes_decrypt_block(block, key)
        plaintext += xor_bytes(decrypted_block, previous_block)
        previous_block = block
    return unpad(plaintext)

# OFB-Modus
def ofb_encrypt_decrypt(plaintext, key, iv):
    ciphertext = b''
    previous_block = iv
    for i in range(0, len(plaintext), 16):
        encrypted_block = aes_encrypt_block(previous_block, key)
        block = plaintext[i:i + 16]
        ciphertext += xor_bytes(block, encrypted_block[:len(block)])
        previous_block = encrypted_block
    return ciphertext

# CTR-Modus
def ctr_encrypt_decrypt(plaintext, key, nonce):
    ciphertext = b''
    counter = 0
    for i in range(0, len(plaintext), 16):
        counter_bytes = nonce + counter.to_bytes(8, byteorder='big')
        encrypted_block = aes_encrypt_block(counter_bytes, key)
        block = plaintext[i:i + 16]
        ciphertext += xor_bytes(block, encrypted_block[:len(block)])
        counter += 1
    return ciphertext