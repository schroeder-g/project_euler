from collections import defaultdict


def sieve_of_eratosthenes(max):
    nums = {i: True for i in range(2, max + 1)}
    for i in range(2, max + 1):
        if nums[i]:
            j = i + i
            while j <= max:
                nums[j] = False
                j += i

    return {i for i in nums.keys() if nums[i]}


def gen_primes():
    composites = defaultdict(list)  # Map composites to lists of primes that divide them
    q = 2
    while True:
        if q not in composites:

            yield q
            composites[q * q] = [q]
        else:
            # q is composite; update the composites
            for p in composites[q]:
                composites[p + q].append(p)
            del composites[q]  # Remove the current composite number
        q += 1
