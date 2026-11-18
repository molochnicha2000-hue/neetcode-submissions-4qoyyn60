class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort(reverse = True)
        adj = collections.defaultdict(list)
        for u, v in tickets:
            adj[u].append(v)
        
        self.ans = []
        def dfs(node):
            while adj[node]:
                cur = adj[node].pop()
                dfs(cur)
            self.ans.append(node)
        dfs('JFK')
        return self.ans[::-1]
