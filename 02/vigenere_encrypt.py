import sys

def encrypt(text, key):
    encrypted_text = ""
    key_length = len(key)
    for i, char in enumerate(text):
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shift = ord(key[i % key_length].upper()) - ord('A')
            encrypted_char = chr((ord(char) - base + shift) % 26 + base)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Verwendung: python vigenere_encrypt.py [Inputfile] [Schlüssel] [Outputfile]")
        sys.exit(1)

    input_file = sys.argv[1]
    key = sys.argv[2].upper()
    output_file = sys.argv[3]

    with open(input_file, 'r') as file:
        text = file.read()
        encrypted_text = encrypt(text, key)

    with open(output_file, 'w') as file:
        file.write(encrypted_text)
        print("Text wurde verschlüsselt und in", output_file, "gespeichert.")
