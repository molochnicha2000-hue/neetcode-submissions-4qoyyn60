class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for x in nums:
            y = abs(x)
            if nums[y - 1] < 0 : return y
            nums[y - 1] = -nums[y - 1]