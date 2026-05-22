class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        N = len(nums)
        res = nums[0]

        pf = sf = 0

        for i in range(N):
            pf = nums[i] * (pf or 1)
            sf = nums[N - i - 1] * (sf or 1)
            res = max(res, max(pf, sf))
        return res