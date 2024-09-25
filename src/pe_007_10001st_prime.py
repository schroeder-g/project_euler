from project_euler.pe_003_largest_prime_factor import is_prime


def get_nth_prime(n):
    primes = []

    curr = 2
    while len(primes) < n:
        if is_prime(curr):
            primes.append(curr)
        curr += 1

    print(primes[-1])
