# RSA Encryption and Decryption in Python

This Python script provides an implementation of the RSA algorithm for encryption and decryption of data.

## Functions

The script includes the following functions:

- `encrypt_decrypt(n, e_or_d, message)`: Encrypts or decrypts a message using the provided key (e_or_d) and modulus (n).
- `multiply(x, m, n)`: Performs the modular exponentiation operation used in RSA.

## Usage

To use this script, you need to have the message, the key (either public or private), and the modulus. These are read from input and key files. The result is written to an output file.

Here is an example of how to use the script:

```bash
python rsa.py input.txt key.txt output.txt