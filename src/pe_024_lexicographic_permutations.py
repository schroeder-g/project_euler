from itertools import permutations


def get_permutations_of_0_thru_9():
    p = permutations(range(10))
    return sorted(list(p))[999999]
