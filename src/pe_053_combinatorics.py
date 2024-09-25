from scipy.special import binom


# https://projecteuler.net/problem=53
def combinatoric_selections():
    out = []
    for n in range(0, 101):
        for r in range(1, n):
            ways_to_choose = binom(n, r)
            if ways_to_choose >= 1000000:
                out.append((n, r))

    print(out, len(out))


combinatoric_selections()
