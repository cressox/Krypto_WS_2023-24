import sys, random


def find_prime(length=1024):
    p = 4
    while not is_prime(p, 10):
        p = generate_prime_candidate(length)
    return p
def generate_prime_candidate(length):
    # Generiert eine ungerade Zufallszahl
    p = random.getrandbits(length)
    p |= (1 << length - 1) | 1
    return p
def is_prime(n, k=5):  # Wiederholen Sie den Miller-Rabin-Test k-mal
    for _ in range(k):
        if not miller_rabin(n):
            return False
    return True
def miller_rabin(p):
    d = p - 1
    r = 0
    while (d % 2) == 0:
        d //= 2
        r += 1
    a = random.randrange(2, p - 1)
    x = (a ** d) % p
    if x == 1 or x == p - 1:
        return True
    while r > 1:
        x = (x * x) % p
        if x == 1:
            return False
        if x == p - 1:
            return True
        r -= 1
    return False
def multiply(base, exponent, modulo):
    y = 1
    m_bin = exponent[2:]  # Konvertiert m in Binär und entfernt das "0b"
    for bit in m_bin:
        y = (y * y) % modulo  # Quadrieren von y bei jedem Schritt
        if bit == '1':
            y = (y * base) % modulo  # Multiplizieren, wenn das aktuelle Bit 1 ist
    return y

def find_random_g(p, q):
    while True:
        g = random.randrange(2, p - 1)
        if pow(g, 2, p) != 1 and pow(g, q, p) != 1:
            return g

def diffie_hellman_key_exchange(p, g):
    a = random.randrange(2, p - 1)
    b = random.randrange(2, p - 1)
    A = pow(g, a, p)
    B = pow(g, b, p)
    S_a = pow(B, a, p)
    S_b = pow(A, b, p)
    assert S_a == S_b, "Shared secrets do not match"
    return p, g, A, B, S_a


if __name__=="__main__":
    if len(sys.argv) != 2:
        print("Usage: Programmname <Bitlänge der Primzahl>")
        sys.exit(1)

    length = int(sys.argv[1])
    p = find_prime(length)
    q = find_prime(length)
    while abs(p - q) < (1 << (length // 2)):
        q = find_prime(length)
    g = find_random_g(p, q)
    p, g, A, B, S = diffie_hellman_key_exchange(p, g)

    with open("output.txt", 'w') as f:
        f.write(f"{p}\n{g}\n{A}\n{B}\n{S}")