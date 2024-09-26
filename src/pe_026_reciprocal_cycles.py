from heapq import heappush, heappop
import decimal


from maths.is_prime import is_prime
from maths.get_factors import get_factors
from maths.get_multiplicative_order import get_multiplicative_order
from maths.sieve_of_eratosthenes import sieve_of_eratosthenes

print(sieve_of_eratosthenes(1000))

# Taken from https://oeis.org/A003592


def gen_terminating_reciprocals():
    heap = [1]
    seen = set(heap)

    while True:
        value = heappop(heap)

        yield value  # On generators: https://chatgpt.com/share/66eb89dd-4e70-800b-a167-5837cd38848d
        seen.remove(value)

        for x in 2 * value, 5 * value:
            if x not in seen:
                heappush(heap, x)
                seen.add(x)


def gen_unterminating_reciprocals(min=1, max=10) -> [int]:
    decimal.getcontext().prec = 1000

    heap = [min]
    value = None

    while heap.__len__ and (not value or value < max):
        value = heappop(heap)
        heappush(heap, value + 1)

        if has_reciprocal_cycle(value):
            reciprocal = decimal.Decimal("1") / decimal.Decimal(str(value))
            yield (value, str(reciprocal))


def has_reciprocal_cycle(n):
    factors = get_factors(n)

    for num in factors:
        if is_prime(num) and num not in [2, 5]:
            # print(f'{n}: prime factor found:', num, )
            return True
    # print('no prime!!!!!')
    return False


cycle_lengths = []
for p in sorted(list(sieve_of_eratosthenes(1000))):
    greatest_cycle_length = 1

    if p not in [2, 5, 1]:
        # Because, apparently this is how the length of the cycle is determined
        # https://en.wikipedia.org/wiki/Repeating_decimal#Fractions_with_prime_denominators
        cycle_length = get_multiplicative_order(p, 10)
        cycle_lengths.append((p, cycle_length))


max_tuple = max(cycle_lengths, key=lambda t: t[1])
print(max_tuple)
