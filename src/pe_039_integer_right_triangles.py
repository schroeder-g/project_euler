from math import sqrt
from project_euler.utils.is_integral import is_integral


def get_hypotenuse(a, b):
    return int(sqrt(a**2 + b**2))


def get_right_tri_perimeter(a, b):
    return a + b + get_hypotenuse(a, b)


def find_most_common_right_triangle_perimeter():
    counts = {n: set() for n in range(1, 1002)}

    for a in range(1, 1001):
        for b in range(1, 1001):
            p = get_right_tri_perimeter(a, b)
            if not is_integral(sqrt(a**2 + b**2)) or p >= 1000:
                continue
            counts[p].add(tuple(sorted([a, b, get_hypotenuse(a, b)])))

    return {
        k: {len(v): v}
        for k, v in counts.items()
        if len(v) == max([len(c) for c in counts.values()])
    }
