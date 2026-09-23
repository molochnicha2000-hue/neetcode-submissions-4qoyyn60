class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = collections.defaultdict(list)
        for u, v, w in times:
            adj[u].append((v, w))

        inf = float('inf')
        visit = [inf] * (n + 1)
        visit[0] = 0
        h = [(0, k)]
        while len(h) > 0:
            w, node = heapq.heappop(h)
            if visit[node] <= w:
                continue
            visit[node] = w
            for nei, nw in adj[node]:
                heapq.heappush(h, (nw + w, nei))
        if inf in visit : return -1
        return max(visit)
