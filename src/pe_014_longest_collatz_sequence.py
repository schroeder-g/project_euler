def gen_collatz(n):
    sequence = [n]

    i = n
    while not i == 1:
        i = i / 2 if i % 2 == 0 else i * 3 + 1
        sequence.append(round(i))

    return sequence


def get_largest_collatz(l, r):
    series = [(i, len(gen_collatz(i))) for i in range(l, r)]

    num_max_ = (0, 0)

    for n, len_ in series:
        if len_ > num_max_[1]:
            num_max_ = (n, len_)

    return num_max_
