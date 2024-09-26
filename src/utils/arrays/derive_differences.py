from collections import defaultdict


def get_frequency_of_differences(_list: [float | int]):
    frequencies = defaultdict(set)

    for n1 in _list:
        for n2 in filter(lambda n: n != n1, _list):
            print(n1, n2)
            diff = abs(int(n1) - int(n2))
            frequencies[diff].add(n1)
            frequencies[diff].add(n2)
    print(frequencies, "\n\n")
    return frequencies
