class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        l = 0
        for current, value in enumerate(nums):
            if value != 0:
                nums[l], nums[current] = nums[current], nums[l]
                l += 1