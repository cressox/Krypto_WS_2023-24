# Diffie-Hellman Key Exchange in Python

This Python script provides an implementation of the Diffie-Hellman key exchange algorithm.

## Functions

The script includes the following functions:

- `find_prime(length=1024)`: Finds a prime number of a certain bit length.
- `generate_prime_candidate(length)`: Generates a random prime candidate.
- `is_prime(n, k=5)`: Checks if a number is prime using the Miller-Rabin test.
- `miller_rabin(p)`: Implements the Miller-Rabin primality test.
- `multiply(base, exponent, modulo)`: Performs the modular exponentiation operation used in Diffie-Hellman.
- `find_random_g(p, q)`: Finds a generator for the group used in Diffie-Hellman.
- `diffie_hellman_key_exchange(p, g)`: Performs the Diffie-Hellman key exchange.

## Usage

To use this script, you need to run it from the command line with one argument: the bit length of the prime numbers.

Here is an example of how to use the script:

```bash
python diffie_hellman.py 1024