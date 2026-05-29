class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        N = len(intervals)
        res = []

        for i in range(N):
            cur = intervals[i]
            if cur[0] > newInterval[1]:
                res.append(newInterval)
                return res + intervals[i :]
            elif cur[1] < newInterval[0]:
                res.append(cur)
            else:
                newInterval = [min(newInterval[0], cur[0]), max(newInterval[1], cur[1])]
        res.append(newInterval)
        return res