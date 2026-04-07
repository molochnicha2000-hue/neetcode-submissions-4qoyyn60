class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda i: i[0])

        prevEnd = intervals[0][1]
        
        res = 0
        for start, end in intervals[1:]:
            if prevEnd > start:
                res += 1
                prevEnd = min(prevEnd, end)
            else:
                prevEnd = end


        return res
        