"""
Find all the pairs of two integers in an unsorted array that sum up to a given S.
For example, if the array is [3, 5, 2, -4, 8, 11] and the sum is 7,
your program should return [[11, -4], [2, 5]] because 11 + -4 = 7 and 2 + 5 = 7.
"""


def find_all_sums_equal_to_s(arr, s):
    solution = []
    int_set = set()

    for int in arr:
        if s - int in int_set:
            solution.append([int, (s - int)])
        if int not in int_set:
            int_set.add(int)

    print(int_set)

    return solution


find_all_sums_equal_to_s([3, 5, 2, -4, 8, 11], 7)
