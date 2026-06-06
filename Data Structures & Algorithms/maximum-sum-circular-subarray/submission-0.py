class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        res = float("-inf")
        N = len(nums)
        for i in range(N):
            cur = 0
            for j in range(i, i + N):
                cur += nums[j % N]
                res = max(res, cur)
        return res