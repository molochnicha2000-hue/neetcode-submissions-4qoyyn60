class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n: return True

        adg = {i:[] for i in range(n)}
        for n1, n2 in edges:
            adg[n1].append(n2)
            adg[n2].append(n1)

        visitSet = set()
        def dfs(i, prev):
            if i in visitSet:
                return False

            visitSet.add(i)
            for j in adg[i]:
                if j == prev: continue
                if not dfs(j, i): return False     
            return True
            
        print(adg) and print(edges)
        return dfs(0, -1) and len(visitSet) == n

