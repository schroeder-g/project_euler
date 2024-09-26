def rotate_matrix(m):
    # Base Cases: empty matrix or non-square matrix
    if len(m) == 0 or len(m) != len(m[0]):
        return False

    ans = []
    n = len(m)

    for layer in range(n / 2):
        # TODO: complete
        pass

    return ans


if __name__ == "__main__":
    t = [
        [0, 1, 2, 3],
        [4, 5, 6, 7],
        [8, 9, 10, 11],
        [12, 13, 14, 15],
    ]
    print(rotate_matrix(t))
