class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        N = len(values)
        adg = collections.defaultdict(list)

        for index, (ai, bi) in enumerate(equations):
            adg[ai].append((bi, values[index]))
            adg[bi].append((ai, 1 / values[index]))

        def dfs(cur, need, visited):
            if cur not in adg or need not in adg:
                return float(-1)
            
            if cur in visited:
                return float(-1)

            if cur == need:
                return 1
            visited.add(cur)

            for nei, weight in adg[cur]:
                if nei not in visited:
                    c = dfs(nei, need, visited)
                    if c != float('-1'):
                        return weight * c





            return -1
        res = []
        for ai, bi in queries:
            cur = dfs(ai, bi, set())
            res.append(cur)

        return res
        