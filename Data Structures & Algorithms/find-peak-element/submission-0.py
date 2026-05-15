class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        res = max(nums)
        return nums.index(res)
        