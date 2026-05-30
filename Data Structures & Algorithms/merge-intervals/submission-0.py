class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #newInterval = [min(intervals[i], intervals[i + 1], 
        #              max(intervals[i], intervals[i + 1]))
        N = len(intervals)
        res = []
        intervals.sort(key = lambda x: x[0])
        cur = intervals[0]

        for i in range(1, N):
            new = intervals[i]
            if cur[1] < new[0]:
                res.append(cur)
                cur = intervals[i]
            else: #cur[1] > new[0]:
                cur = [min(cur[0], intervals[i][0]), 
                      max(intervals[i][1], cur[1])]
        res.append(cur)
       #print(res)
        return res
