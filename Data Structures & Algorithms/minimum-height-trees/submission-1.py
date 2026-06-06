class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if not edges:
            return [0]
        adg = {i : [] for i in range(n)}

        for ai, bi in edges:
            adg[ai].append(bi)
            adg[bi].append(ai)

        def dfs(node):
            if node in visit:
                return 0

            best = float("-inf")
            visit.add(node)
            for nei in adg[node]:
                best = max(best, dfs(nei) + 1)
            return best

        visit = set()
        res = collections.defaultdict(set)
        for ai, bi in edges:
            first = dfs(ai)
            res[first].add(ai)
            visit.clear()
            second = dfs(bi)
            res[second].add(bi)
            visit.clear()

        #print(adg)
        #print(res)
        for digit in sorted(res.keys()):
            return list(res[digit])