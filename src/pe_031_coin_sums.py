def get_number_of_coins_that_make_2_pounds():
    return count_ways_to_make_change([1, 2, 5, 10, 20, 50, 100, 200], 200)


def count_ways_to_make_change(atoms: [int], target: int):
    # Each index represents the number of combinations (ways) to reach the indexed value.
    # As such we want the target-th element from ways.
    ways = [0 for k in range(target + 1)]

    # Can only reach 0 with no atoms.
    ways[0] = 1

    # Iterate through atoms,
    for atom in atoms:
        # For each atom starting at the atom-th index
        for j in range(atom, target + 1):
            # increment the sub-solution by the number of combinations
            # in the last index touched by the atom
            ways[j] += ways[j - atom]

    return ways[target]
