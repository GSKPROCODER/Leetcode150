from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        l = 0
        for current, value in enumerate(nums):
            if value != 0:
                nums[l], nums[current] = nums[current], nums[l]
                l += 1

nums = [0, 1, 0, 3, 12]
solution = Solution()
solution.moveZeroes(nums)
print(nums)
