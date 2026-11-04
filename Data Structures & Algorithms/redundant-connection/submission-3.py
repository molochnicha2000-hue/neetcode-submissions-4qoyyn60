class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = max(max(x, y) for x, y in edges)
        par = [i for i in range(n + 1)]
        sz = [1] * (n + 1)

        def find(x):
            if par[x] != x:
                par[x] = find(par[x])
            return par[x]
            
        def union(x, y):
            p1, p2 = find(x), find(y)
            if p1 == p2:
                return True
            if sz[p1] > sz[p2]:
                sz[p1] += sz[p2]
                par[p2] = p1
            else:
                sz[p2] += sz[p1]
                par[p1] = p2
            return False
        
        for x, y in edges:
            if union(x, y):
                return [x, y]
            