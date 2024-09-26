class Solution:
    def __init__(self):
        self.memo = {}

    def rob(self, nums) -> int:
        self.memo = {}

        return self.rob_from(0, nums)

    def rob_from(self, i, nums):
        if i >= len(nums):
            return 0
        if i in self.memo:
            return self.memo[i]

        # recursive evaluation to solve subproblems
        ans = max(self.rob_from(i + 1, nums), self.rob_from(i + 2, nums) + nums[i])
        self.memo[i] = ans
        return ans


test = [1, 2, 4, 1, 1, 5]

driver = Solution()
print("The maximum value you can ransack from this street is:", driver.rob(test))
