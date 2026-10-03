"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, arr: List[Interval]) -> int:
        arr = [[x.start, x.end] for x in arr]
        arr.sort()
        h = []
        for l, r in arr:
            if h and h[0] <= l:
                heapq.heappop(h)
            heapq.heappush(h, r)
        return len(h)