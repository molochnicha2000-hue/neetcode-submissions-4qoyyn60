class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = collections.defaultdict(list)
        for u, v, t in times:
            adj[u].append((v, t))
        
        h = [(0, k)]
        visit = [math.inf] * (n + 1)
        visit[k] = visit[0] = 0
        while len(h) > 0:
            t, node = heapq.heappop(h)
            if t != visit[node] : continue
            for nei, dt in adj[node]:
                nt = dt + t
                if visit[nei] > nt:
                    visit[nei] = nt
                    heapq.heappush(h, (nt, nei))

        r = max(visit)
        return r if r != math.inf else -1

        