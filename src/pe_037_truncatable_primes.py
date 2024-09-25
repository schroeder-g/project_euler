from project_euler.utils.sieve_of_eratosthenes import sieve_of_eratosthenes


def find_sum_of_truncatable_primes():
    primes = sieve_of_eratosthenes(1000000)
    truncatable = {3797, 797, 37}

    for p in primes:
        if p not in [2, 3, 5, 7, 3797, 797, 37] and all(
            [int(n) in primes for n in [str(p)[0], str(p)[-1]]]
        ):
            # print("HA", p)
            passes = True
            # Check removals l -> r
            str_p = str(p)
            for _ in range(len(str_p) - 1):
                str_p = str_p[1:]
                if int(str_p) in primes:
                    continue
                else:
                    passes = False

            # Check removals r -> l
            str_p = str(p)
            for _ in range(len(str_p) - 1):
                str_p = str_p[:-1]
                if int(str_p) in primes:
                    continue
                else:
                    passes = False

            if passes:
                truncatable.add(p)

    print(truncatable, len(truncatable))
    return sum(truncatable)
