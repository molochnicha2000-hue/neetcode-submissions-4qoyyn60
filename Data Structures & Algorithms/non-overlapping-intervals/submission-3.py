from functools import cache
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        N = len(intervals)
        intervals.sort()

        @cache
        def dfs(i, prev):
            if i == N:
                return 0
            
            best = dfs(i + 1, prev)
            if prev == float('inf') or intervals[prev][1] <= intervals[i][0]:
                current = 1 + dfs(i + 1, i)
                best = max(best, current)
            return best
        
        return N - dfs(0, float('inf'))