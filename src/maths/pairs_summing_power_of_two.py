"""Implements the two pointer technique to find all pairs in an array that
produce a sum that is a power of 2. Pairs are inclusive, here meaning that
all possible pairs of (X,Y) include (X,X)."""

from math import log2

def pairs_summing_power_of_two(nums):
    if len(nums) == 0:
        return 0

    ans = 0
    sorted_nums = sorted(nums)
    left = 0
    right = len(sorted_nums) - 1
    while left < right:
        sum_of_pair = sorted_nums[left] + sorted_nums[right]
        min_sum = sorted_nums[left] * 2
        max_sum = sorted_nums[right] * 2

        # If either left + left or plus right is equal to the current power of two,
        # increment the answer by 1 and move the left index to the right by one
        # (returning to beginning of while loop).

        if sum_of_pair > 0 and log2(sum_of_pair).is_integer() or \
                min_sum > 0 and log2(min_sum).is_integer():
            if min_sum > 0 and log2(min_sum).is_integer():
                print(sorted_nums[left], "+", sorted_nums[left], "=", min_sum)
            else:
                print(sorted_nums[left], "+", sorted_nums[right], "=", sum_of_pair)
            ans += 1
            left += 1
        elif max_sum > 0 and log2(max_sum).is_integer():
            print(sorted_nums[right], "+", sorted_nums[right], "=", max_sum)
            ans += 1
            right -= 1
        elif sum_of_pair > 0 and  and not log2(sum_of_pair).is_integer():
        else:
            left += 1
    return ans


test_array = [-1, 0, 1, 2, 3, 4, 5]

print("________\ntotal number of pairs \nsumming to a power of 2: \n",
      pairs_summing_power_of_two(test_array))
