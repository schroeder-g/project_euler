# TODO: Handle leading zeroes
def rotate_int(n, right=True, steps=1):
    s = steps % n
    return int(str(n)[-s:] + str(n)[:-s]) if right else int(str(n)[s:] + str(n)[:s])
