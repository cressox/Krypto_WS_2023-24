import sys

def encrypt_decrypt(n, e_or_d, message):
    return multiply(x=message, m=e_or_d, n=n)    

def multiply(x, m, n):
    y = 1
    m_bin = m[2:]  # Konvertiert m in Binär und entfernt das "0b"
    for bit in m_bin:
        y = (y * y) % n  # Quadrieren von y bei jedem Schritt
        if bit == '1':
            y = (y * x) % n  # Multiplizieren, wenn das aktuelle Bit 1 ist
    return y

if __name__=="__main__":
    if len(sys.argv) != 4:
        print("Usage: Programmname <Input-Datei> <Schlüssel-Datei> <Output-Datei>")
        sys.exit(1)

    input_file = sys.argv[1]
    key_file = sys.argv[2]
    output_file = sys.argv[3]

    # Input-Datei lesen
    with open(input_file, 'r') as f:
        message = int(f.read().strip())

    # Schlüssel-Datei lesen
    with open(key_file, 'r') as f:
        e_or_d = bin(int(f.readline().strip()))  # Erste Zeile: e oder d
        n = int(f.readline().strip())

    # Verschlüsseln / Entschlüsseln durchführen
    result = encrypt_decrypt(n, e_or_d, message)

    # Output in Datei schreiben
    with open(output_file, 'w') as f:
        f.write(str(result))

    print("Operation erfolgreich durchgeführt. Ergebnis in", output_file, "geschrieben.")