from math import floor, sqrt


def is_prime(n):
    if n in [0, 1, 2]:
        return True

    for num in range(abs(n))[2:]:
        if is_factor(n, num):
            return False
    return True


def is_factor(i, div):
    if div == 0:
        return False
    return True if i % div == 0 else False


def get_largest_prime_factor(n):
    factors = []
    base_divisor = 2
    while base_divisor <= sqrt(n):
        if is_factor(n, base_divisor):
            factors.extend([base_divisor, floor(n / base_divisor)])

        base_divisor += 1

    for num in sorted(factors, reverse=True):
        # print(f"check factor {n}")
        if is_prime(num):
            print(f"The biggest prime factor of {n} is {num}")
            return

    print("no prime factors :(")
