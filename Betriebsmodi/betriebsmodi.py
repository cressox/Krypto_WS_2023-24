
t = 11 # Blocklänge

# Blackbox-Verschlüsselungsfunktion
def encrypt_block(plaintext_block, key):
    # Hier implementieren Sie die Verschlüsselung eines einzelnen Blocks
    # Verwenden Sie den Schlüssel, um den Block zu verschlüsseln
    # Beispiel: Hier können Sie AES, DES oder eine andere Verschlüsselung verwenden
    # Rückgabe des verschlüsselten Blocks
    encrypted_block = plaintext_block  # Dummy-Implementierung, bitte ersetzen
    return encrypted_block

# Blackbox-Entschlüsselungsfunktion
def decrypt_block(ciphertext_block, key):
    # Hier implementieren Sie die Entschlüsselung eines einzelnen Blocks
    # Verwenden Sie den Schlüssel, um den Block zu entschlüsseln
    # Beispiel: Hier können Sie AES, DES oder eine andere Entschlüsselung verwenden
    # Rückgabe des entschlüsselten Blocks
    decrypted_block = ciphertext_block  # Dummy-Implementierung, bitte ersetzen
    return decrypted_block

# ECB-Verschlüsselung
def ecb_encrypt(plaintext, key, t):
    # Nachricht mit Nullen auffüllen auf ein Vielfaches von t
    plaintext = plaintext.ljust((len(plaintext) + t - 1) // t * t, b'\x00')
    ciphertext = b''
    
    # Blockweise Verschlüsselung
    for i in range(0, len(plaintext), t):
        block = plaintext[i:i + t]
        encrypted_block = encrypt_block(block, key)
        ciphertext += encrypted_block
    
    return ciphertext

# ECB-Entschlüsselung
def ecb_decrypt(ciphertext, key, t):
    plaintext = b''
    
    # Blockweise Entschlüsselung
    for i in range(0, len(ciphertext), t):
        block = ciphertext[i:i + t]
        decrypted_block = decrypt_block(block, key)
        plaintext += decrypted_block
    
    return plaintext

# CBC-Verschlüsselung
def cbc_encrypt(plaintext, key, t, iv=b'\x00' * t):
    plaintext = plaintext.ljust((len(plaintext) + t - 1) // t * t, b'\x00')
    ciphertext = b''
    previous_block = iv
    
    for i in range(0, len(plaintext), t):
        block = plaintext[i:i + t]
        xor_result = bytes(x ^ y for x, y in zip(block, previous_block))
        encrypted_block = encrypt_block(xor_result, key)
        ciphertext += encrypted_block
        previous_block = encrypted_block
    
    return ciphertext

# CBC-Entschlüsselung
def cbc_decrypt(ciphertext, key, t, iv=b'\x00' * t):
    plaintext = b''
    previous_block = iv
    
    for i in range(0, len(ciphertext), t):
        block = ciphertext[i:i + t]
        decrypted_block = decrypt_block(block, key)
        xor_result = bytes(x ^ y for x, y in zip(decrypted_block, previous_block))
        plaintext += xor_result
        previous_block = block
    
    return plaintext

# OFB-Verschlüsselung
def ofb_encrypt(plaintext, key, t, iv=b'\x00' * t):
    ciphertext = b''
    previous_block = iv
    
    for i in range(0, len(plaintext), t):
        encrypted_block = encrypt_block(previous_block, key)
        block = plaintext[i:i + t]
        xor_result = bytes(x ^ y for x, y in zip(block, encrypted_block))
        ciphertext += xor_result
        previous_block = encrypted_block
    
    return ciphertext

# OFB-Entschlüsselung
def ofb_decrypt(ciphertext, key, t, iv=b'\x00' * t):
    return ofb_encrypt(ciphertext, key, t, iv)  # OFB ist selbstentschlüsselnd

# CTR-Verschlüsselung
def ctr_encrypt(plaintext, key, t, iv=b'\x00' * t):
    ciphertext = b''
    counter = int.from_bytes(iv, 'big')
    
    for i in range(0, len(plaintext), t):
        counter_bytes = counter.to_bytes(t, 'big')
        encrypted_block = encrypt_block(counter_bytes, key)
        block = plaintext[i:i + t]
        xor_result = bytes(x ^ y for x, y in zip(block, encrypted_block))
        ciphertext += xor_result
        counter += 1
    
    return ciphertext

# CTR-Entschlüsselung
def ctr_decrypt(ciphertext, key, t, iv=b'\x00' * t):
    return ctr_encrypt(ciphertext, key, t, iv)  # CTR ist selbstentschlüsselnd