from math import pow


def get_sum_square(n):
    return sum([i * i for i in range(n + 1)])


def get_square_sum(n):
    return pow(sum(range(n + 1)), 2)


def get_square_sum_difference(n):
    return get_square_sum(n) - get_sum_square(n)
