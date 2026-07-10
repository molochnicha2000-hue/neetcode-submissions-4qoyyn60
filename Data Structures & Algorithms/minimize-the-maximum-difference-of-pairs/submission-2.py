class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        N = len(nums)
        nums.sort()
        def good(target):
            pa = 0
            i = 0
            while i < N - 1:
                if abs(nums[i + 1] - nums[i]) <= target:
                    pa += 1
                    i += 2
                else:
                    i += 1
                if pa == p:
                    return True
            return pa == p
        
        
        l, r = 0, max(nums)
        res = r
        while l <= r:
            m = (l + r) // 2
            if good(m):
                res = min(res, m)
                r = m - 1
            else:
                l = m + 1
        return res

        
        