class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        ans = 0
        for x in nums:
            if x - 1 not in s:
                l = 1
                while x + l in s:
                    l += 1
                ans = max(ans, l)
        return ans

        