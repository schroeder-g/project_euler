from maths.sieve_of_eratosthenes import gen_primes
from maths.is_prime import is_prime


def consecutive_prime_sum():
    g_primes = gen_primes()
    partial_sums = {}
    primes_set = set({next(g_primes), next(g_primes), next(g_primes)})
    primes = [2, 3, 5]
    partial_sums[2] = 1
    partial_sums[5] = 2
    partial_sums[8] = 3

    max_ = 3

    for p in g_primes:

        primes.append(p)
        primes_set.add(p)

        if p > 500000:
            break

        curr_sum = p
        curr_sum_prime_count = 1
        # @TODO: ordered set
        for i, p2 in enumerate(primes[-2::-1]):

            # time.sleep(.5)

            curr_sum += p2
            curr_sum_prime_count += 1

            if curr_sum > 1000000:
                break

            if is_prime(curr_sum):
                existing = partial_sums.get(curr_sum)
                if (
                    not existing
                    or curr_sum_prime_count > existing
                    and curr_sum_prime_count > max_
                ):
                    max_ = curr_sum_prime_count
                    # print(f'{p} | {curr_sum} + {p2} = {curr_sum + p2}')
                    # print(f'count: {curr_sum_prime_count}')
                    partial_sums[curr_sum] = curr_sum_prime_count

    print(f"there are {len(primes)} valued less than 1 mill")
    [
        print(p)
        for p in list(
            map(
                lambda p: f"{p[0]} – {p[1]} primes",
                sorted(dict.items(partial_sums), key=lambda item: item[0] / item[1]),
            )
        )[0:10]
    ]


# big_p = (0, -1)
# for p in primes[-1::-1]:
#     if partial_sums.get(p) and partial_sums[p] > big_p[1]:
#         print(p, partial_sums[p])
#         big_p = (p, (partial_sums[p]))


# print(big_p)

# return sum_

consecutive_prime_sum()
