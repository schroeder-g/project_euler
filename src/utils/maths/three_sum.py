class Solution:
    """
    A function that finds all unique combinations of three numbers within an array that sum to zero.
    Input: nums -> An array of numbers
    Operations: Sort array of nums. For each (non-duplicate) number in given array,
                cast two pointers that span
    """

    def threeSum(self, nums):
        ans = []
        nums.sort()

        # Iterate through sorted nums looking for compliment
        for i in range(len(nums)):
            if nums[i] > 0:
                # All later indices store positive values; no sum == 0 possible.
                break
            if i == 0 or nums[i - 1] != nums[i]:
                self.twoSumII(nums, i, ans)

        return ans

    def twoSumII(self, nums, i, res):
        # Initialize left and right pointers
        l, r = i + 1, len(nums) - 1
        while l < r:
            sum_ = nums[l] + nums[r] + nums[i]
            if sum_ < 0:
                l += 1
            elif sum_ > 0:
                r -= 1
            else:
                res.append([nums[i], nums[l], nums[r]])
                l, r = l + 1, r - 1

                # Skip duplicates summing to zero
                while l < r and nums[l] == nums[l - 1]:
                    l += 1
