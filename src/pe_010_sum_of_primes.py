# Generate the list of primes less than n
def sieve_of_eratosthenes(range_):
    nums = {i: True for i in range(2, range_ + 1)}
    for i in range(2, range_ + 1):
        if nums[i]:
            j = i + i
            while j <= range_:
                nums[j] = False
                j += i

    return [i for i in nums.keys() if nums[i]]
