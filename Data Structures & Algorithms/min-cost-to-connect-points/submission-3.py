class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        adj = collections.defaultdict(list)
        for i in range(N):
            x1, y1 = points[i]
            for j in range(i + 1, N):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append((j, dist))
                adj[j].append((i, dist))

        q = collections.deque([0])
        visit = set()
        heap = [(0, 0)]
        cost = 0
        while len(visit) < N:
            dist, node = heapq.heappop(heap)
            if node in visit:
                continue

            cost += dist
            visit.add(node)
            for nei, d in adj[node]:
                if nei in visit:
                    continue
                heapq.heappush(heap, (d, nei))

        return cost
