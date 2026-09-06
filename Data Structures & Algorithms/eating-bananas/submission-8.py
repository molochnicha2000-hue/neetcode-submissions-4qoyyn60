class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        N = len(piles)
        def good(speed):
            count = 0
            for x in piles:
                count += math.ceil(x / speed)
            return count <= h

        l, r = 1, 10 ** 20
        while l <= r:
            m = (l + r) >> 1
            if good(m):
                res = m
                r = m - 1
            else:
                l = m + 1
        return res