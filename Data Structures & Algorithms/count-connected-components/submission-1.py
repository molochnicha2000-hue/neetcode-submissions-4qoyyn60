class uf:
    def __init__(self, n):
        self.par = [ i for i in range(n)]
        self.size = [1] * n

    def find(self, x):
        if x != self.par[x]:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x, y):
        p1, p2 = self.find(x), self.find(y)
        if p1 == p2:
            return False
        if self.size[p1] > self.size[p2]:
            self.par[p2] = p1
            self.size[p1] += self.size[p2]
        else:
            self.par[p1] = p2
            self.size[p1] += self.size[p2]
        return True

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uv = uf(n)
        for u, v in edges:
            uv.union(u, v)
        res = set([uv.find(x) for x in uv.par])
        return len(res)