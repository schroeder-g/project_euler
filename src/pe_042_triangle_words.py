from project_euler.utils.score_word import score_word
from project_euler.utils.read_out_file import read_out_file


words = read_out_file("triangle_words")


def is_triangle_number(n):
    left = 0
    right = n
    while left <= right:
        poly = (left + right) // 2
        prod = poly**2 + poly
        print(poly, prod)
        if prod < 2 * n:
            left = poly + 1
        elif prod > 2 * n:
            right = poly - 1
        else:
            return True

    return False


def count_triangle_words():
    return sum([1 if is_triangle_number(score_word(w)) else 0 for w in words])
