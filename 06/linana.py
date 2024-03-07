# Vorläufige Annahmen und Definitionen
s_box_inv = {0xE: 0, 0x4: 1, 0xD: 2, 0x1: 3, 0x2: 4, 0xF: 5, 0xB: 6, 0x8: 7, 0x3: 8, 0xA: 9, 0x6: 10, 0xC: 11, 0x5: 12, 0x9: 13, 0x0: 14, 0x7: 15}
M = [("Klartext1", "Kryptotext1"), ("Klartext2", "Kryptotext2")]  # Beispiel für Klartext-Kryptotext-Paare

# Initialisierung der Zählvariable für jeden möglichen Teilschlüssel
alpha = {(L1, L2): 0 for L1 in range(16) for L2 in range(16)}

# Durchlauf aller Klartext-Kryptotext-Paare
for x, y in M:
    for L1 in range(16):
        for L2 in range(16):
            # Berechnung der inversen S-Box-Werte
            v4_2 = L1 ^ int(y[2], 16)  # y[2] sollte den relevanten Teil des Kryptotextes darstellen
            v4_4 = L2 ^ int(y[4], 16)
            u4_2 = s_box_inv[v4_2]
            u4_4 = s_box_inv[v4_4]

            # Überprüfung der linearen Approximation
            if int(x[5]) ^ int(x[7]) ^ int(x[8]) ^ u4_2 ^ u4_4 == 0:  # x[5], x[7], etc. sollten die relevanten Bits des Klartextes darstellen
                alpha[(L1, L2)] += 1

# Finden des Teilschlüssels mit der größten Abweichung
max_diff = -1
max_key = None
t = len(M)  # Anzahl der Klartext-Kryptotext-Paare
for key, count in alpha.items():
    diff = abs(count - (t / 2))
    if diff > max_diff:
        max_diff = diff
        max_key = key

# Ausgabe des wahrscheinlichsten Teilschlüssels
print(f"Der wahrscheinlichste Teilschlüssel ist: {max_key}")
