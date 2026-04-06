class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if not edges:
            return n

        if n == 0:
            return 1

        adg = {i:set() for i in range(n)}

        
        for i, j in edges:# connections of graf
            adg[i].add(j)
            adg[j].add(i)

        visit = set()
        res = 0
        def dfs(curr_n):
            visit.add(curr_n)

            for ad in adg[curr_n]:
                if ad not in visit:
                    dfs(ad)

            
        for i in range(n):
            if i not in visit:
                res +=1
                dfs(i)
        return res
        