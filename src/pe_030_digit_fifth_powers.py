def get_sum_of_digits_to_fifth_power(n):
    return sum([int(num) ** 5 for num in str(n)])


def get_nums_equal_to_sum_of_digits_to_the_fifth():
    seq = []
    for num in 1, range(1, 10000000):
        if num == get_sum_of_digits_to_fifth_power(num):
            seq.append(num)
    print(seq)
    return sum(seq) - 1
