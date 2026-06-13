class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        N = len(weights)
        l, r = max(weights), sum(weights)

        def good(limit):
            res, cur = 1, limit
            for w in weights:
                if cur - w < 0:
                    res += 1
                    if res > days:
                        return False
                    cur = limit
                cur -= w
            return True

        res = r
        while l <= r:
            mid = (l + r) // 2
            if good(mid):
                res = min(res, mid)
                r = mid - 1
            else:
                l = mid + 1
        return res
        