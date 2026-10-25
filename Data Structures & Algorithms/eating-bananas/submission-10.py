class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def good(k):
            return sum(math.ceil(x / k) for x in piles) <= h
        l, r = 1, 10 ** 20
        while l <= r:
            m = (l + r) // 2
            if good(m) :
                r = m - 1
                res = m
            else:
                l = m + 1
        return res