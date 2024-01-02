import sys

def encrypt(text, key):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            encrypted_char = chr((ord(char) - base + key) % 26 + base)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Verwendung: python encrypt.py [input.txt] [Schlüssel] [output.txt]")
        sys.exit(1)

    input_file = sys.argv[1]
    key = int(sys.argv[2])
    output_file = sys.argv[3]

    with open(input_file, 'r') as file:
        text = file.read()
        encrypted_text = encrypt(text, key)

    with open(output_file, 'w') as file:
        file.write(encrypted_text)
        print("Text wurde verschlüsselt und in", output_file, "gespeichert.")
