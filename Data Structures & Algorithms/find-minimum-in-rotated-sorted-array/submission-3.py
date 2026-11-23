class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        def dfs(l, r):
            if l == r : return nums[l]
            m = (l + r) // 2
            if nums[m] > nums[-1]:
                return dfs(m + 1, r)
            return dfs(l, m)
        return dfs(0, n - 1)
