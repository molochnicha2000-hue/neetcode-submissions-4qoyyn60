class Solution:
    def mySqrt(self, x: int) -> int:
        if not x: return 0
        if x == 1: return 1
        l,r = 0, x - 1
        res = -1
        while l <= r:
            m = (l + r) // 2
            if pow(m, 2) <= x:
                res = max(res, m)
                l = m + 1
            else:
                r = m - 1
        return res
