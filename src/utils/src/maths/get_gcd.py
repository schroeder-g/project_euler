def gcd(a: int, b: int) -> int:
    """returns the greatest common denominator of two integers"""
    if a == 0 or b == 0:
        return 0
    elif a == b:
        return a

    return gcd(a - b, b) if (a > b) else gcd(a, b - a)
