class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        numi = set(nums)
        n = float("inf")
        for i in nums:
            if i >= 0:
                n = min(n, i)
        if n == float("inf"):
            return 1
        # prev
        for i in range(1, n + 1, 1):
            if not i in numi:
                return i
        
        res = n
        while n + 1 in numi:
            n += 1
            res = n
        return res + 1