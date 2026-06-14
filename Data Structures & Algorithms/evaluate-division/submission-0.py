class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        N = len(values)
        adg = collections.defaultdict(list)

        for index, (ai, bi) in enumerate(equations):
            adg[ai].append((bi, values[index]))
            adg[bi].append((ai, 1 / values[index]))

        def dfs(cur, need):
            if cur not in adg or need not in adg:
                return float(-1)
            
            q = collections.deque([(cur, 1)])
            visit = set()
            while q:
                cur, value = q.popleft()
                if cur == need:
                    return value
                if cur in visit:
                    continue

                visit.add(cur)
                for (nei, weight) in adg[cur]:
                    q.append((nei, value * weight))
            return -1
        res = []
        for ai, bi in queries:
            cur = dfs(ai, bi)
            res.append(cur)

        return res
        