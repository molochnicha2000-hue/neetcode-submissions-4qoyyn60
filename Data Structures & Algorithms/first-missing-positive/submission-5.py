class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        N = len(nums)
        worst_key = N + 1
        nums = set(nums)

        res = 1
        while res != worst_key:
            if res not in nums:
                return res
            res += 1
        return res