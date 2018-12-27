#!/usr/bin/env python3
# A collection of algorithms for generating prime numbers


def brute_force(count=100):
    primes = [2]
    n = 3
    while len(primes) < count:
        if is_prime(n):
            primes.append(n)
        n += 1
    return primes


def is_prime(n):
    mid = int(n ** 0.5)
    for factor in range(2, mid + 1):
        if n % factor == 0:
            return False
    return True


def prime_factors(count=100):
    primes = [2]
    n = 3
    while len(primes) < count:
        mid = int(n ** 0.5)
        is_prime = True
        for prime in primes:
            if prime > mid:
                break
            if n % prime == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(n)
        n += 1
    return primes


def sieve(count=100, size_factor=15):
    size = count * size_factor
    sieve = [True] * size
    # premark 0 and 1 as non-prime
    sieve[0] = sieve[1] = False
    # geometric mean as midpoint
    mid = int(len(sieve) ** 0.5)

    prime = 2
    while prime <= mid:
        for multiple in range(prime + prime, len(sieve), prime):
            sieve[multiple] = False
        # advance one and scan forward to the next True value for next prime
        prime += 1
        while not sieve[prime]:
            prime += 1

    primes = [n for n, is_prime in enumerate(sieve) if is_prime]
    if len(primes) > count:
        primes = primes[:count]
    return primes


if __name__ == "__main__":
    import sys

    show_only_final = False
    limit = 100  # default to finding first 100 primes
    if len(sys.argv) > 1:
        limit = int(sys.argv[1])

    # primes = brute_force(limit)
    # primes = prime_factors(limit)
    primes = sieve(limit)

    if show_only_final:
        print(primes[-1])
    else:
        for p in primes:
            print(p)