class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        globMin, globMax = 1, 1
        for i in range(len(nums)):
            tmp = globMax * nums[i]
            globMax = max(nums[i] * globMin, globMax * nums[i], nums[i])
            globMin = min(nums[i] * globMin, tmp, nums[i])
            res = max(res, globMax)
        return res