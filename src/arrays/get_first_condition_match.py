from typing import Callable, Any


def get_first_condition_match(s: list, q: Callable[[int, *Any]], *args):
    """
    First argument of q must be the index of the series being checked
    args are passed to q callback
    """
    i = 0
    while True:
        if q(s[i], *args):
            return s[i]

        if i == len(s) - 1:
            print("No numbers in this series satisfy condition q.")
            break
        i += 1
