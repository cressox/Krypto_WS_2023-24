# Import necessary libraries
import sys
import re
import collections

# Function to decrypt the text using a given key
def decrypt(text, key):
    decrypted_text = ""
    for char in text:
        if char.isalpha():  # Check if the character is an alphabet
            base = ord('A') if char.isupper() else ord('a')  # Determine the ASCII value of the base ('A' for uppercase, 'a' for lowercase)
            decrypted_char = chr((ord(char) - base - key) % 26 + base)  # Decrypt the character
            decrypted_text += decrypted_char
        else:
            decrypted_text += char  # If not an alphabet, keep the character as it is
    return decrypted_text

# Function to perform frequency analysis on the text
def frequency_analysis(text):
    letters = re.findall(r'[A-Za-z]', text)  # Find all alphabets in the text
    frequencies = collections.Counter(letters)  # Count the frequency of each alphabet
    sorted_frequencies = sorted(frequencies.items(), key=lambda x: x[1], reverse=True)  # Sort the frequencies in descending order
    most_common_letter = sorted_frequencies[0][0]  # Get the most common letter
    key = ord(most_common_letter) - ord('E')  # Assume the most common letter is 'E' to get the key
    return key

# Main function
if __name__ == "__main__":
    if len(sys.argv) != 2:  # Check if the number of command line arguments is correct
        print("Verwendung: python decrypt_auto.py [input.txt]")
        sys.exit(1)

    input_file = sys.argv[1]  # Get the input file name from the command line arguments

    with open(input_file, 'r') as file:  # Open the input file
        text = file.read()  # Read the text from the input file
        key = frequency_analysis(text)  # Perform frequency analysis to get the key

    decrypted_text = decrypt(text, key)  # Decrypt the text using the key

    output_file = "decrypted_" + input_file  # Create the output file name
    with open(output_file, 'w') as file:  # Open the output file
        file.write(f"Schlüssel: {key}\n")  # Write the key to the output file
        file.write(decrypted_text)  # Write the decrypted text to the output file
        print(f"Text wurde entschlüsselt und in {output_file} gespeichert.")  # Print a success message