inf = float('inf')
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        N = len(nums)
        res = nums[0]
        MIN, MAX = 1, 1
        current = 1

        for x in nums:
            current = MAX * x
            MIN, MAX = min(MAX * x, MIN * x, x), max(MIN * x, MAX * x, x)
            res = max(res, MAX)
        return res
