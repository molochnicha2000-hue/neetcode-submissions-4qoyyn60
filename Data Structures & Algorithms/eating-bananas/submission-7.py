class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        def check(s):
            time = 0
            for i in piles:
                time += math.ceil(i / s)
            return time

        INF = 10 ** 32 - 1
        res = INF
        while l <= r:
            mid = (l + r) // 2
            if check(mid) <= h:
                res = min(res, mid)
                r = mid - 1
                #return mid
            elif check(mid) > h:
                l = mid + 1
        return res
            