# Additive Chiffre

Die additive Chiffre ist eine einfache Verschlüsselungsmethode, die auf einer Verschiebung des Alphabets basiert. In diesem Repository finden Sie drei Python-Programme zur Verschlüsselung, Entschlüsselung und automatischen Entschlüsselung von Texten mit der additiven Chiffre.

## Programme

1. [**encrypt.py**](encrypt.py) - Programm zur Verschlüsselung von Texten.

   - **Verwendung:** `python encrypt.py [input.txt] [Schlüssel] [output.txt]`
   - **Beispiel:**
     ```
     python encrypt.py input.txt 3 output.txt
     ```

2. [**decrypt.py**](decrypt.py) - Programm zur Entschlüsselung von Texten.

   - **Verwendung:** `python decrypt.py [input.txt] [Schlüssel] [output.txt]`
   - **Beispiel:**
     ```
     python decrypt.py input.txt 3 output.txt
     ```

3. [**auto_decrypt.py**](auto_decrypt.py) - Programm zur automatischen Entschlüsselung von Texten mit Hilfe der Häufigkeitsanalyse.

   - **Verwendung:** `python auto_decrypt.py [input.txt]`
   - **Beispiel:**
     ```
     python auto_decrypt.py input.txt
     ```

## Beispiel

Um die Programme zu verwenden, können Sie die folgenden Schritte befolgen:

1. **Verschlüsselung**:
   - Rufen Sie `encrypt.py` auf, um Text zu verschlüsseln. Geben Sie die Eingabedatei, den Schlüssel und die Ausgabedatei an.
   - Beispiel: `python encrypt.py input.txt 3 output.txt`

2. **Entschlüsselung**:
   - Rufen Sie `decrypt.py` auf, um verschlüsselten Text zu entschlüsseln. Geben Sie die Eingabedatei, den Schlüssel und die Ausgabedatei an.
   - Beispiel: `python decrypt.py input.txt 3 output.txt`

3. **Automatische Entschlüsselung**:
   - Rufen Sie `auto_decrypt.py` auf, um Text automatisch zu entschlüsseln. Geben Sie die verschlüsselte Eingabedatei an.
   - Beispiel: `python auto_decrypt.py input.txt`

Die Ausgabe wird in den angegebenen Ausgabedateien gespeichert.

---

Hinweis: Bitte stellen Sie sicher, dass Sie die Python-Programme im gleichen Verzeichnis wie Ihre Textdateien haben oder den Pfad zur Textdatei angeben.
