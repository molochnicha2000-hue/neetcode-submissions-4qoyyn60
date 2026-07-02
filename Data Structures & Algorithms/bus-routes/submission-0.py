class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        N = len(routes)
        adj = collections.defaultdict(list)

        for i in range(N):
            cur = routes[i]
            for j in cur:
                for h in cur:
                    if j != h:
                        adj[j].append(h)
        
        def bfs(src, target):
            q = collections.deque([(src, 0)])
            visit = set([src])

            while q:
                route, steps = q.popleft()
                if route == target:
                    return steps
                
                for nei in adj[route]:
                    if nei != route and nei not in visit:
                        visit.add(nei)
                        q.append((nei, steps + 1))
            return -1
        return bfs(source, target)