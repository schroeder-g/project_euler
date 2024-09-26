from project_euler.utils.get_coprime import is_coprime


def get_multiplicative_order(n, a):
    """
    A function to determine the smallest positive initeger k (the order) for which a^k === 1 (mod n)
    https://en.wikipedia.org/wiki/Multiplicative_order
    """
    if not is_coprime(n, a):
        print("ye")
        raise Exception("Unable to get mult. order")

    exp = 1

    while not (pow(a, exp) - 1) % n == 0:
        exp += 1

    return exp
