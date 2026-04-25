class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        nums1 = set(nums)
        for ind, n in enumerate(nums):
            if not (n - 1) in nums:
                curr = 1
                
                while n + 1 in nums1:
                    #ind += 1
                    n = n + 1
                    curr += 1
                res = max(res, curr)
        return res
                    

        