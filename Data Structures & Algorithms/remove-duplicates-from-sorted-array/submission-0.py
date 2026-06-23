import sortedcontainers
class Solution:
    def removeDuplicates(self, nums: List[int]) -> List[int]:
        res = sortedcontainers.SortedSet()
        N = len(nums)
        for n in nums:
            res.add(n)
            
        res = list(res)
        nums[::] = res
        return len(nums)