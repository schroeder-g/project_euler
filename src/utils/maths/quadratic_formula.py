from math import sqrt


def quad(a, b, c):
    sq_d = sqrt(pow(b, 2) - (4 * a * c))

    return ((-b + sq_d) / (2 * a), (-b - sq_d) / (2 * a))
