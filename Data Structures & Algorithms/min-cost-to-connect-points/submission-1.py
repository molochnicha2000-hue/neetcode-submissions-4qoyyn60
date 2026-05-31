class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        adg = {i : [] for i in range(N)}

        for i in range(N):
            cur = points[i]
            for j in range(i + 1, N):
                new = points[j]
                dist = abs(cur[0] - new[0]) + abs(cur[1] - new[1])
                adg[i].append((dist, j))
                adg[j].append((dist, i))
        #print(adg)
        res = 0
        minH = [(0, 0)]
        visit = set()
        while len(visit) != N:
            cdist, node = heapq.heappop(minH)
            if node in visit:
                continue

            visit.add(node)
            res += cdist
            for dist, nei in adg[node]:
                if nei not in visit:
                    heapq.heappush(minH, (dist, nei))
        return res