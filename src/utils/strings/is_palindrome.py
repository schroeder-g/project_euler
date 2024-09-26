from math import floor, ceil


def is_palindrome(s):
    len_ = len(s)
    return s[: floor(len_ / 2)] == s[len_ : ceil(len_ / 2) - 1 : -1]
