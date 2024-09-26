"""
Given a list of integers and a target value, return the indices of the two numbers in the list that add up to a specific target.

*Note: You can assume that each input has exactly one solution, and the same element cannot be used more than once.*

Example:

Given nums = [3, 8, 12, 17], target = 15,

Because nums[0] + nums[2] = 3 + 12 = 15,
return [0, 2].
"""

""" Dictionaries don't keep track of duplicates.
    Keys and values are unique"""


def two_sum(nums, target):
    map = {element: index for index, element in enumerate(nums)}

    for i in range(len(nums)):
        diff = target - nums[i]

        # check if the difference is in map
        if diff in map:
            return [i, map[diff]]

        # otherwise, we don't have numbers that sum to target.

    return "No two numbers add up to target"


nums = [1, 2, 3, 4, 5]
target = 9
print(two_sum(nums, target))
