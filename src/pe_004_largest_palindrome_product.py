from math import floor, ceil


def get_largest_palindrome_product():
    products = []
    for i in range(500, 1000):
        for j in range(500, 1000):
            if is_palindrome(str(i * j)):
                products.append(i * j)

    print(max(products))


def is_palindrome(s):
    len_ = len(s)
    return s[: floor(len_ / 2)] == s[len_ : ceil(len_ / 2) - 1 : -1]
