from functools import cache
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        N = len(startTime)
        arr = []
        for start, end, prof in zip(startTime, endTime, profit):
            arr.append((start, end, prof))
        
        arr.sort()
        @cache
        def dfs(index, prev):
            if index >= N:
                return 0
            
            best = dfs(index + 1, prev)

            l, r = arr[index][:2]
            if prev <= l:
                best = max(best, arr[index][2] + dfs(index + 1, arr[index][1]))
            return best

        res = dfs(0, -1)
        dfs.cache_clear()
        return res
