import sys

def decrypt(text, key):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            decrypted_char = chr((ord(char) - base - key) % 26 + base)
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Verwendung: python decrypt.py [input.txt] [Schlüssel] [output.txt]")
        sys.exit(1)

    input_file = sys.argv[1]
    key = int(sys.argv[2])
    output_file = sys.argv[3]

    with open(input_file, 'r') as file:
        text = file.read()
        decrypted_text = decrypt(text, key)

    with open(output_file, 'w') as file:
        file.write(decrypted_text)
        print("Text wurde entschlüsselt und in", output_file, "gespeichert.")
