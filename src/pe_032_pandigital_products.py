import os
from itertools import permutations
from project_euler.utils.partitions import get_integer_partition_permutations
from project_euler.utils.read_out_file import read_out_file


def is_pandigital(mul1, mul2, product):
    whole_str = f"{mul1}{mul2}{product}"
    return (
        False
        if len(whole_str) != len(set(whole_str))
        or any([int(n) > len(whole_str) for n in whole_str])
        else True
    )


# print(is_pandigital(39,186,7254))


permute_file_path = os.path.expanduser(
    "~/scripts/py/src/project_euler/out/permutations_1_to_9.txt"
)
pandigitals_file_path = os.path.expanduser(
    "~/scripts/py/src/project_euler/out/pan_digital_products.txt"
)


def write_permutations_1_to_9():
    perms = []
    for i in range(2, 10):
        i_perms = list(
            filter(
                lambda v: "0" not in v,
                [
                    "".join([str(c) for c in t])
                    for t in permutations([n for n in range(1, i + 1)], i)
                ],
            )
        )
        perms += i_perms

    with open(permute_file_path, "a") as file:
        file.write(str(perms) + "\n")
    print(len(perms))


def check_for_multiplicands():
    pandigital_products = set()

    for number_string in read_out_file():
        partitions = get_integer_partition_permutations(len(number_string), 3)
        for part in partitions:
            i1, i2, i3 = part[0], part[1], part[2]
            m1, m2, product = (
                int(number_string[0:i1]),
                int(number_string[i1 : i1 + i2]),
                int(number_string[i1 + i2 :]),
            )

            if m1 < product and m2 < product and m1 * m2 == product:
                print(f"{m1} x {m2} = {product}")
                pandigital_products.add(product)

    with open(pandigitals_file_path, "a") as file:
        file.write(str(pandigital_products) + "\n")
    print(sum(pandigital_products))


check_for_multiplicands()
