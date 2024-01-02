# Verschlüsselungsmodi mit Blocklänge t

In diesem Repository finden Sie Python-Funktionen für verschiedene Verschlüsselungsmodi mit einer vorgegebenen Blocklänge `t`. Diese Funktionen verwenden eine Blackbox-Verschlüsselungsfunktion `encrypt_block` und `decrypt_block` für die Verschlüsselung und Entschlüsselung von Einzelblöcken.

## Funktionen

1. **ECB-Verschlüsselung (`ecb_encrypt` und `ecb_decrypt`)**

   - **Verwendung für die Verschlüsselung:** `ecb_encrypt(plaintext, key, t)`
   - **Verwendung für die Entschlüsselung:** `ecb_decrypt(ciphertext, key, t)`

2. **CBC-Verschlüsselung (`cbc_encrypt` und `cbc_decrypt`)**

   - **Verwendung für die Verschlüsselung:** `cbc_encrypt(plaintext, key, t, iv)`
   - **Verwendung für die Entschlüsselung:** `cbc_decrypt(ciphertext, key, t, iv)`

3. **OFB-Verschlüsselung (`ofb_encrypt` und `ofb_decrypt`)**

   - **Verwendung für die Verschlüsselung:** `ofb_encrypt(plaintext, key, t, iv)`
   - **Verwendung für die Entschlüsselung:** `ofb_decrypt(ciphertext, key, t, iv)`

4. **CTR-Verschlüsselung (`ctr_encrypt` und `ctr_decrypt`)**

   - **Verwendung für die Verschlüsselung:** `ctr_encrypt(plaintext, key, t, iv)`
   - **Verwendung für die Entschlüsselung:** `ctr_decrypt(ciphertext, key, t, iv)`

## Beispielverwendung

```python
t = 11  # Blocklänge

# Hier müssen Sie die Blackbox-Verschlüsselungsfunktionen `encrypt_block` und `decrypt_block` implementieren.

# Beispiel für ECB-Verschlüsselung
plaintext = b"This is a test."
key = b"my_secret_key"
ciphertext = ecb_encrypt(plaintext, key, t)
decrypted_text = ecb_decrypt(ciphertext, key, t)

# Beispiel für CBC-Verschlüsselung
plaintext = b"This is another test."
key = b"my_secret_key"
iv = b"random_iv_12345"
ciphertext = cbc_encrypt(plaintext, key, t, iv)
decrypted_text = cbc_decrypt(ciphertext, key, t, iv)

# Beispiel für OFB-Verschlüsselung
plaintext = b"Yet another test."
key = b"my_secret_key"
iv = b"random_iv_54321"
ciphertext = ofb_encrypt(plaintext, key, t, iv)
decrypted_text = ofb_decrypt(ciphertext, key, t, iv)

# Beispiel für CTR-Verschlüsselung
plaintext = b"CTR mode test."
key = b"my_secret_key"
iv = b"initial_ctr_999"
ciphertext = ctr_encrypt(plaintext, key, t, iv)
decrypted_text = ctr_decrypt(ciphertext, key, t, iv)
