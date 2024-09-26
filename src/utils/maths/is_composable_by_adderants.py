from maths.get_sums_to_target import get_summing_permutations


def is_composable_by_adderants(target: int or float, adds: [int or float]):
    result = []
    get_summing_permutations(adds, target, 0, result, [], exit_on_solution=True)

    return not not len(result)
