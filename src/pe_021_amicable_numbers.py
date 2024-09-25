from project_euler.utils.get_factors import get_factors


def get_amicable_nums(start, end):
    amicable_nums = []
    for num in range(start, end + 1):
        factor_sum = sum(get_factors(num))
        if sum(get_factors(factor_sum)) == num and factor_sum != num:
            amicable_nums.extend([factor_sum, num])

    print(amicable_nums)
    return sum(set(amicable_nums))
