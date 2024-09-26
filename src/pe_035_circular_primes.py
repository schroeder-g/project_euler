from maths.is_prime import is_prime
from maths.rotate_int_int import rotate_int
from maths.sieve_of_eratosthenes import sieve_of_eratosthenes


def count_circular_primes():
    primes: dict = sieve_of_eratosthenes(1000000)
    circular_primes = []

    def is_circular_prime(n):
        rotated = rotate_int(n)

        while rotated != n:
            if rotated == n:
                break

            if rotated in primes or is_prime(rotated):
                rotated = rotate_int(rotated)
                continue
            else:
                return False

        return True

    for prime in primes:
        if is_circular_prime(prime):
            print(prime)
            circular_primes.append(prime)

    print(sorted(list(set(circular_primes))))
    return len(set(circular_primes))
