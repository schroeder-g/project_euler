from maths.get_gcd import gcd


def is_coprime(a, b):

    if gcd(a, b) == 1:
        return True
    else:
        return False
