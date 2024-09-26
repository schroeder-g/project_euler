from collections import OrderedDict
from maths.get_factors import reduce_to_prime_factors


# https://projecteuler.net/problem=47
def find_four_consecutive_primes():
    prime_factor_map = OrderedDict()

    n = 1
    while len(prime_factor_map) < 4:
        # print(n)
        n_factors = reduce_to_prime_factors(n)
        if len(n_factors) == 4:
            prime_factor_map[n] = n_factors
        elif len(prime_factor_map):
            prime_factor_map = OrderedDict()

        n += 1

    return prime_factor_map.popitem(last=False)

    # pass


print(find_four_consecutive_primes())
