# Vigenère-Chiffre

Die Vigenère-Chiffre ist eine polyalphabetische Substitutionstechnik, die auf der Verwendung von Schlüsselwörtern basiert. In diesem Repository finden Sie zwei Python-Programme zur Verschlüsselung und automatischen Entschlüsselung von Texten mit der Vigenère-Chiffre.

## Programme

1. [**vigenere_encrypt.py**](vigenere_encrypt.py) - Programm zur Verschlüsselung von Texten.

   - **Verwendung:** `python vigenere_encrypt.py [Inputfile] [Schlüssel] [Outputfile]`
   - **Beispiel:**
     ```
     python vigenere_encrypt.py input.txt SCHLUESSEL output.txt
     ```

2. [**vigenere_auto_decrypt.py**](vigenere_auto_decrypt.py) - Programm zur automatischen Entschlüsselung von Vigenère-verschlüsselten Texten.

   - **Verwendung:** `python vigenere_auto_decrypt.py [Inputfile] [Outputfile]`
   - **Beispiel:**
     ```
     python vigenere_auto_decrypt.py input.txt output.txt
     ```

## Beispiel

Um die Programme zu verwenden, können Sie die folgenden Schritte befolgen:

1. **Verschlüsselung**:
   - Rufen Sie `vigenere_encrypt.py` auf, um Text zu verschlüsseln. Geben Sie die Eingabedatei, den Schlüssel und die Ausgabedatei an.
   - Beispiel: `python vigenere_encrypt.py input.txt SCHLUESSEL output.txt`

2. **Automatische Entschlüsselung**:
   - Rufen Sie `vigenere_auto_decrypt.py` auf, um Text automatisch zu entschlüsseln. Geben Sie die verschlüsselte Eingabedatei an.
   - Beispiel: `python vigenere_auto_decrypt.py input.txt output.txt`

Die Ausgabe wird in den angegebenen Ausgabedateien gespeichert.

---

Hinweis: Bitte stellen Sie sicher, dass Sie die Python-Programme im gleichen Verzeichnis wie Ihre Textdateien haben oder den Pfad zur Textdatei angeben. Ersetzen Sie "SCHLUESSEL" durch Ihren gewünschten Schlüssel.
