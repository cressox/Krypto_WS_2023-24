import sys
import re
import collections

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

def frequency_analysis(text):
    letters = re.findall(r'[A-Za-z]', text)
    frequencies = collections.Counter(letters)
    sorted_frequencies = sorted(frequencies.items(), key=lambda x: x[1], reverse=True)
    most_common_letter = sorted_frequencies[0][0]
    key = ord(most_common_letter) - ord('E')
    return key

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Verwendung: python decrypt_auto.py [input.txt]")
        sys.exit(1)

    input_file = sys.argv[1]

    with open(input_file, 'r') as file:
        text = file.read()
        key = frequency_analysis(text)

    decrypted_text = decrypt(text, key)

    output_file = "decrypted_" + input_file
    with open(output_file, 'w') as file:
        file.write(f"Schlüssel: {key}\n")
        file.write(decrypted_text)
        print(f"Text wurde entschlüsselt und in {output_file} gespeichert.")
