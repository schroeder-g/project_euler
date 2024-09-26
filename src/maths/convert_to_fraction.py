import math


def fractions(num, den):
    if math.gcd(num, den) == den:
        return int(num / den)
    elif math.gcd(num, den) == 1:
        return str(num) + "/" + str(den)
    else:
        top = num / math.gcd(num, den)
        bottom = den / math.gcd(num, den)
        return str(top) + "/" + str(bottom)
