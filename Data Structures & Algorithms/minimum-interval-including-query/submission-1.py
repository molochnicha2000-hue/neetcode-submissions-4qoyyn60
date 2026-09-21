class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        N = len(intervals)
        intervals.sort(key = lambda x : x[0])
        queries = sorted([(x, i) for i, x in enumerate(queries)])


        r = 0
        heap = []
        ans = [-1] * len(queries)
        for need, i in queries:
            while r < N and intervals[r][0] <= need:
                L = intervals[r][1] - intervals[r][0] + 1
                heapq.heappush(heap, (L, intervals[r][1]))
                r += 1

            while len(heap) > 0 and heap[0][1] < need:
                heapq.heappop(heap)

            if len(heap) > 0:
                ans[i] = heap[0][0]
        return ans    