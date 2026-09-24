class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = [i for i in range(n)]
        sz = [1] * n
        def union(x, y):
            p1, p2 = find(x), find(y)
            if p1 == p2 : return
            if sz[p1] > sz[p2]:
                sz[p1] += sz[p2]
                par[p2] = p1
            else:
                sz[p2] += sz[p1]
                par[p1] = p2
        def find(x):
            if par[x] != x:
                par[x] = find(par[x])
            return par[x]
        
        for u, v in edges:
            union(u, v)
        
        return len(set([find(x) for x in par]))