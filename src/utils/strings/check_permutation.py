from collections import Counter


def check_permutation(s1, s2):
    d1, d2 = dict(Counter(s1)), dict(Counter(s2))
    return d1 == d2


print(check_permutation("Alex", "xelA"))
