from maths.is_prime import is_prime
from arrays.flatten import flatten
from functools import reduce


def get_factors(n):
    return (
        [0]
        if n == 0
        else list(
            set(
                filter(
                    lambda _n: _n != n and _n != 1,
                    reduce(
                        list.__add__,
                        ([i, n // i] for i in range(1, int(n**0.5) + 1) if n % i == 0),
                    ),
                )
            )
        )
    )


def get_common_factors(*args):
    return list(
        reduce(
            lambda s1, s2: set.intersection(s1, s2),
            [set(get_factors(n)) for n in args],
        )
    )


def reduce_to_prime_factors(n):
    if isinstance(n, int) and (n in [0, 1, 2] or is_prime(n)):
        return [n]

    factor_list = n if isinstance(n, list) else [n]

    if all(map(lambda f: is_prime(f), factor_list)):
        return factor_list

    # get factors/ return recurse on factors
    return reduce_to_prime_factors(
        list(set(flatten(map(lambda f: get_factors(f), factor_list))))
    )
