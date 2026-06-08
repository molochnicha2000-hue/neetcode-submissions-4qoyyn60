class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def dfs(src, adg, visit, path, order):
            if src in path:
                return False

            if src in visit:
                return True   
            path.add(src)
            visit.add(src)
            for nei in adg[src]:
                if not dfs(nei, adg, visit, path, order):
                    return False
            path.remove(src)
            order.append(src)
            return True

        def topo_sort(edges):
            adg = defaultdict(list)
            for src, dst in edges:
                adg[src].append(dst)

            visit, path = set(), set()
            order = []
            for src in range(1, k + 1):
                if not dfs(src, adg, visit, path, order):
                    return []
            return order[::-1]
        
        first, second = topo_sort(rowConditions), topo_sort(colConditions)
        if not first or not second:
            return []

        res = [[0] * k for i in range(k)]
        new_f = {n: i for i, n in enumerate(first)}
        new_s = {n: i for i, n in enumerate(second)}

        for j in range(1, k + 1):
            r, c = new_f[j], new_s[j]
            res[r][c] = j

        return res




    