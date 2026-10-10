from functools import cache
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = collections.defaultdict(list)
        for u, v, c in flights:
            adj[u].append((v, c))
        @cache
        def dfs(node, k):
            if node == dst : return 0
            if k == -1 : return float('inf')
            return min([c + dfs(nei, k - 1) for nei, c in adj[node]] + [float('inf')])
        R = dfs(src, k)
        if R == float('inf') : return -1
        return R