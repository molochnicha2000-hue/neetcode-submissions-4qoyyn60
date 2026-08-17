class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        N = mountainArr.length()
        l, r = 1, N - 2
        while l <= r:
            m = (l + r) // 2
            num = mountainArr.get(m)
            left, right = mountainArr.get(m - 1), mountainArr.get(m + 1)
            
            if left < num < right:
                l = m + 1
            elif left > num > right:
                r = m - 1
            else:
                break

        peak = m
        
        if target == mountainArr.get(peak):
            return peak

        l, r = 0, peak - 1
        while l <= r:
            m = (l + r) // 2
            num = mountainArr.get(m)
            if num == target:
                return m
            elif num > target:
                r = m - 1
            else:
                l = m + 1

        l, r = peak, N - 1
        while l <= r:
            m = (l + r) // 2
            num = mountainArr.get(m)
            if num == target:
                return m
            elif num > target:
                l = m + 1
            else:
                r = m - 1
        return -1
        
                    