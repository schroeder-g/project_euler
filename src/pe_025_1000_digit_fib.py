from collections import OrderedDict


def get_1st_fib_num_with_1000_digits():
    seq = OrderedDict({0: 0, 1: 1})

    def fib_recur(n):
        if n in seq:
            return seq[n]

        if n < 2:
            seq[n] = n
            return n
        # ans = fib(n - 1) + fib(n - 2)
        ans = None
        seq[n] = ans
        return ans

    def fib_it(n):
        for num in range(2, n + 1):
            seq[num] = seq[num - 1] + seq[num - 2]

    fib_it(5000)
    for i in sorted(seq.values()):
        if len(str(i)) == 1000:
            return [k for k in seq.keys() if seq[k] == i]
