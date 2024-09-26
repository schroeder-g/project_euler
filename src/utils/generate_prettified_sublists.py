from numpy import array_split
from numpy.core.defchararray import join as np_join
import numpy as np


def generate_enumerated_sublists(array, n=8):
    d, m = divmod(len(array), n)
    subs = array_split(array, d + (1 if m != 0 else 0))
    for i, arr in enumerate(subs):
        yield " " + "\n ".join(
            [
                f"{len(subs[i - 1]) * i + j + 1}.) " + f"{str(a)}"
                for j, a in enumerate(arr)
            ]
        )
