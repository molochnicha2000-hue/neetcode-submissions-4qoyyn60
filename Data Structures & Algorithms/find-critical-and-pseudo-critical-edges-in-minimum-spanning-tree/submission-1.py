class Solution:
    def findCriticalAndPseudoCriticalEdges(self, N: int, edges: List[List[int]]) -> List[List[int]]:
        for i, edge in enumerate(edges):
            edge.append(i)

        adj = {i : [] for i in range(N)}
        for ai, bi, weight, idx in edges:
            adj[ai].append((bi, weight, idx))
            adj[bi].append((ai, weight, idx))
        
        pseudo = [] # pseudo and critical
        critical = []
        def minim(src, dst, exclude_idx):
            dist = [float("inf")] * N
            dist[src] = 0
            pq = [(0, src)]

            while pq:
                max_w, u = heapq.heappop(pq)
                if u == dst:
                    return max_w

                for v, weight, idx in adj[u]:
                    if idx == exclude_idx:
                        continue
                    new_w = max(max_w, weight)
                    if new_w < dist[v]:
                        dist[v] = new_w
                        heapq.heappush(pq, (new_w, v))
            return dist[dst]

        for i, (u, v, w, idx) in enumerate(edges):
            if w < minim(u, v, idx):
                critical.append(idx)

            elif w == minim(u, v, -2):
                pseudo.append(idx)
        return [critical, pseudo]