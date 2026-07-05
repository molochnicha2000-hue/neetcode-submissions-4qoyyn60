class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        N = len(nums)
        res = float("-inf")

        for i in range(N):
            j = i + 1
            total = nums[i]
            res = max(res, total)
            while j != i:
                total += nums[j % N]
                j = (j + 1) % N
                res = max(res, total)
        return res