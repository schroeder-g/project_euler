def get_adderants(vals, target):
    result = []
    get_summing_permutations(vals, target, 0, result, [])

    return result


def get_summing_permutations(
    vals: [int or float],
    target: int or float,
    i: int,
    solutions: [[int or float]] = None,
    curr: [int or float] = None,
    exit_on_solution: bool = False,
):

    if target < 0 or (exit_on_solution and len(solutions)):
        return
    if target == 0:
        ans = sorted(curr)
        if ans not in solutions:
            solutions.append(ans)
            print("Found a solution!", ans)
        return solutions

    for j in vals[i::]:
        curr.append(j)
        get_summing_permutations(vals, target - j, i, solutions, curr, exit_on_solution)
        del curr[-1]
