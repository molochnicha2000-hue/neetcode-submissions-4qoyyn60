class Solution:
    def minTime(self, N: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        adj = collections.defaultdict(list)

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        need = hasApple.count(True)
        if not need:
            return 0
        
        def dfs(node, prev):
            time = 0
            for nei in adj[node]:
                if nei == prev:
                    continue
                current = dfs(nei, node)
                if not hasApple[nei] and current == 0:
                    continue
                time += current + 2
            return time
        return dfs(0, -1)


