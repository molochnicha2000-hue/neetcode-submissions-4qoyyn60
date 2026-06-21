class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        N = mountainArr.length()
        l, r = 0, N - 1
        res = float("inf")
        peak = 1
        # find peak
        while l <= r:
            m = (l + r) // 2
            if mountainArr.get(m) > mountainArr.get(peak):
                peak = m
                l = m
            else:
                r = m - 1
        
        if mountainArr.get(peak) == target:
            return peak

        # find target in 2 sorted arrays
        l, r = 0, peak - 1
        while l <= r:
            m = (l + r) // 2
            cur = mountainArr.get(m)
            if cur == target:
                return m
            elif cur > target:
                r = m - 1
            else:
                l = m + 1
        if res != float("inf"):
            return res

        l, r = peak, N - 1
        while l <= r:
            m = (l + r) // 2
            cur = mountainArr.get(m)
            if cur == target:
                return m
            elif cur > target:
                l = m + 1
            else:
                r = m - 1


        return res if res != float("inf") else -1