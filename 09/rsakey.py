import sys, random

def key_gen(z):
    pass

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

def eea(a, b):
    k = 0
    r_0, r_1 = a, b
    s_0, s_1 = 1, 0
    t_0, t_1 = 0, 1

    while r_1 != 0:
        k += 1
        q_k = r_0 // r_1  # Verwenden Sie Ganzzahldivision statt Fließkomma-Division

        tmp = r_1
        r_1 = r_0 - q_k * r_1
        r_0 = tmp

        tmp = s_1
        s_1 = s_0 - q_k * s_1
        s_0 = tmp

        tmp = t_1
        t_1 = t_0 - q_k * t_1
        t_0 = tmp

    return r_0, s_0, t_0  # Rückgabe der letzten Werte von r, s und t vor r_1 wird 0

def is_prime(n, k=5):  # Wiederholen Sie den Miller-Rabin-Test k-mal
    for _ in range(k):
        if not miller_rabin(n):
            return False
    return True

def generate_prime_candidate(length):
    # Generiert eine ungerade Zufallszahl
    p = random.getrandbits(length)
    p |= (1 << length - 1) | 1
    return p

def find_prime(length=1024):
    p = 4
    while not is_prime(p, 10):
        p = generate_prime_candidate(length)
    return p

def find_coprime(phi):
    e = 2**16 + 1
    while True:
        gcd, _, _ = eea(e, phi)
        if gcd == 1:
            break
        e += 2
    return e

def generate_keys(length=1024):
    p = find_prime(length)
    q = find_prime(length)
    while abs(p - q) < (1 << (length // 2)):
        q = find_prime(length)
    n = p * q
    phi = (p - 1) * (q - 1)
    e = find_coprime(phi)
    _, d, _ = eea(e, phi)
    d = d % phi
    if d < 0:
        d += phi
    return e, d, n, p, q

if __name__=="__main__":
    if len(sys.argv) != 5:
        print("Usage: Programmname <Länge> <Output privat> <Output öffentlich> <benutzte Primzahlen>")
        sys.exit(1)

    length = int(sys.argv[1])
    output_privat = sys.argv[2]
    output_öffentlich = sys.argv[3]
    benutzte_primzahlen = sys.argv[4]

    e, d, n, p, q = generate_keys(length)

    with open(benutzte_primzahlen, 'w') as f:
        f.write(f"{p}\n{q}\n")

    with open(output_privat, 'w') as f:
        f.write(f"{d}\n{n}\n")

    with open(output_öffentlich, 'w') as f:
        f.write(f"{e}\n{n}\n")