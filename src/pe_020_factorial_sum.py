from math import factorial


def get_factorial_digit_sum(n):
    fact = factorial(n)

    return sum([int(d) for d in str(fact)])
