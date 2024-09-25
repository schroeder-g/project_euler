from math import pow


def is_pythagorean_triplet(a, b, c):
    return pow(a, 2) + pow(b, 2) == pow(c, 2)


# Returns the set of all triplets that sum to n
def three_sum(n):
    tuplets = []
    triplets = set()
    for i in range(1, n):
        tuplets.append([i, n - i])

    for tuplet in tuplets:
        for i in range(1, tuplet[1]):
            trip = frozenset([tuplet[0], i, tuplet[1] - i])
            if not len(trip) == 3:
                continue
            triplets.add(trip)
    return triplets


def get_pythagorean_triplet(n):
    pythagorean_triplets = []
    triplets = three_sum(n)

    for t in triplets:
        if is_pythagorean_triplet(*sorted(t)):
            pythagorean_triplets.append([n for n in t])

    print(pythagorean_triplets)
