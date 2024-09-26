from maths.get_factors import get_factors


def is_abundant_num(n):
    return sum(get_factors(n)) > n


def get_abundant_nums(start, end):
    return [n for n in range(start, end + 1) if is_abundant_num(n)]


def get_all_non_abundant_num_sums():
    abundant_nums = get_abundant_nums(1, 20162)

    abundant_num_sums = {i + j for i in abundant_nums for j in abundant_nums}

    total = 0
    for n in range(1, 20162):
        if n not in abundant_num_sums:
            total += n

    return total
