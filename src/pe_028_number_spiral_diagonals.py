def gen_number_spiral_matrix(h):
    nums = iter(range(h * h, 0, -1))

    matrix = [[-1 for i in range(h)] for i in range(h)]

    x = h - 1
    y = 0
    x_moves = [-1, 0, 1, 0]
    y_moves = [0, 1, 0, -1]
    di = 0

    for n in range(h * h):
        matrix[y][x] = next(nums)

        next_el_out_of_bounds = x + x_moves[di] in [-1, h] or y + y_moves[di] in [-1, h]

        # If out of bounds or next element in direction has been touched, change direction
        if next_el_out_of_bounds or matrix[y + y_moves[di]][x + x_moves[di]] != -1:
            di = (di + 1) % 4

        x += x_moves[di]
        y += y_moves[di]

    return matrix


def get_diagonal_values(m, starts_at_zeroth=True):
    l_ = len(m)
    return (
        [m[i][i] for i in range(l_)]
        if starts_at_zeroth
        else [m[-i - 1][i] for i in range(l_)]
    )


def sum_diagonal_values_for_matrix(m):
    vals = get_diagonal_values(m)
    vals.extend(get_diagonal_values(m, starts_at_zeroth=False))
    return sum(set(vals))
