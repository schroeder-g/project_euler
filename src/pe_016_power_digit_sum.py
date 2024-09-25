def get_sum_of_power_digits(n, power):
    product = pow(n, power)
    return sum([int(num) for num in str(product)])
