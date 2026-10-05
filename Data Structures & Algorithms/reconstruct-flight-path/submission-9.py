class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = collections.defaultdict(list)
        for u, v in sorted(tickets)[::-1]:
            adj[u].append(v)
        

        path = set()
        R = []
        def dfs(src):
            while adj[src]:
                dst = adj[src].pop()
                dfs(dst)
            R.append(src)
        dfs('JFK')
        return R[::-1]
