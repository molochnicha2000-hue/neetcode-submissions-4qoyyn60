class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        visit = set()
        q = collections.deque()
        adg = {i : [] for i in range(N)}
        minHeap = [(0, 0)]

        for i in range(N):
            cx, cy = points[i]
            for j in range(i + 1, N):
                nx, ny = points[j]
                dist = abs(nx - cx) + abs(ny - cy)
                adg[i].append((dist, j))
                adg[j].append((dist, i))
        
        res = 0
        while len(visit) < N:
            cost, point = heapq.heappop(minHeap)
            if point in visit:
                continue
            
            res += cost
            visit.add(point)
            for dist, nei in adg[point]:
                if nei not in visit:
                    heapq.heappush(minHeap, (dist, nei))


        return res
            