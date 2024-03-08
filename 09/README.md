# RSA Key Generation in Python

This Python script provides an implementation of RSA key generation.

## Functions

The script includes the following functions:

- `miller_rabin(p)`: Implements the Miller-Rabin primality test.
- `eea(a, b)`: Implements the Extended Euclidean Algorithm.
- `is_prime(n, k=5)`: Checks if a number is prime using the Miller-Rabin test.
- `generate_prime_candidate(length)`: Generates a random prime candidate.
- `find_prime(length=1024)`: Finds a prime number of a certain bit length.
- `find_coprime(phi)`: Finds a number that is coprime with phi.
- `generate_keys(length=1024)`: Generates a pair of RSA keys.

## Usage

To use this script, you need to run it from the command line with four arguments: the bit length of the keys, the filename for the private key, the filename for the public key, and the filename for the used prime numbers.

Here is an example of how to use the script:

```bash
python rsakey.py 1024 private_key.txt public_key.txt primes.txt