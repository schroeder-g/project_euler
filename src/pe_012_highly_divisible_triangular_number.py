from maths.get_factors import get_factors
from arrays.get_first_condition_match import get_first_condition_match


# var n being the placement in the sequence of triangular numbers
# e.g. n of 3 being 1 + 2 + 3 = 6
def gen_triangular_number(n):
    return sum(num for num in range(1, n + 1))


def has_more_than_j_factors(n, j):
    factors = get_factors(n)
    return len(factors) >= j


def get_first_triangular_num_with_more_than_500_factors():
    triangular_numbers = [gen_triangular_number(n) for n in range(1, 100000)]
    return get_first_condition_match(triangular_numbers, has_more_than_j_factors, 500)
