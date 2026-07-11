class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        N = len(nums)
        
        res = float('-inf')
        for i in range(N):
            current = nums[i]
            res = max(res, current)
            for j in range(i + 1, N):
                current *= nums[j]
                res = max(res, current)
        return res


