import sys
import re
import collections

def decrypt(text, key):
    decrypted_text = ""
    key_length = len(key)
    for i, char in enumerate(text):
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shift = ord(key[i % key_length].upper()) - ord('A')
            decrypted_char = chr((ord(char) - base - shift) % 26 + base)
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text

def frequency_analysis(text):
    letters = re.findall(r'[A-Za-z]', text)
    frequencies = collections.Counter(letters)
    sorted_frequencies = sorted(frequencies.items(), key=lambda x: x[1], reverse=True)
    most_common_letter = sorted_frequencies[0][0]
    key = chr(((ord(most_common_letter) - ord('E')) % 26) + ord('A'))
    return key

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Verwendung: python vigenere_auto_decrypt.py [Inputfile] [Outputfile]")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    with open(input_file, 'r') as file:
        text = file.read()
        key = frequency_analysis(text)

    decrypted_text = decrypt(text, key)

    with open(output_file, 'w') as file:
        file.write(f"Schlüssel: {key}\n")
        file.write(decrypted_text)
        print("Text wurde entschlüsselt und in", output_file, "gespeichert.")
