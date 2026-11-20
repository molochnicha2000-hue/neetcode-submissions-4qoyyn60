class Solution:
    def findOrder(self, n: int, prerequisites: List[List[int]]) -> List[int]:
        adj = collections.defaultdict(list)
        for u, v in prerequisites:
            adj[u].append(v)
        
        self.visit = set()
        self.ans = []
        self.path = set()
        def dfs(node):
            if node in self.path : return False
            if node in self.visit : return True
            self.path.add(node)
            for nei in adj[node]:
                if not dfs(nei) : return False
            self.ans.append(node)
            self.visit.add(node)
            self.path.remove(node)
            return True
        
        for i in range(n):
            if not dfs(i) : return []
        return self.ans