class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = collections.defaultdict(list)
        for u, v in prerequisites:
            adj[u].append(v)
        
        self.visit = set()
        self.res = []
        def dfs(node, path):
            if node in path:
                return False
            if node in self.visit:
                return True
            path.add(node)
            self.visit.add(node)
            for nei in adj[node]:
                if not dfs(nei, path):
                    return False
            self.res.append(node)
            path.remove(node)
            return True

        for i in range(numCourses):
            cur = dfs(i, set())
            if not cur:
                return []
        return self.res
            
        
        