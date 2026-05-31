class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        N = len(nums)
        res = 0
        for i in range(N):
            res ^= nums[i]
            
        return res