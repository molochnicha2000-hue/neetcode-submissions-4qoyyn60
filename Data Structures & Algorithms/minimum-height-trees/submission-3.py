from sortedcontainers import SortedSet
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if not edges:
            return [0]
        adg = {i : [] for i in range(n)}

        for ai, bi in edges:
            adg[ai].append(bi)
            adg[bi].append(ai)

        def bfs(node):
            q = collections.deque([node])
            res = 0
            while q:
                for _ in range(len(q)):
                    cur = q.popleft()
                    visit.add(cur)
                    for nei in adg[cur]:
                        if nei not in visit:
                            q.append(nei)
                res += 1
            return res

        visit = set()
        res = SortedSet()
        wereDone = set()
        for ai, bi in edges:
            if ai not in wereDone:
                first = bfs(ai)
                visit.clear()
                res.add((first, ai))
                wereDone.add(ai)
            if bi not in wereDone:
                second = bfs(bi)
                visit.clear()
                res.add((second, bi))
                wereDone.add(bi)
        wereDone.clear()
        res = list(res)
        N = len(res)
        ans = collections.defaultdict(list)
        prev = res[0][0]
        for val, index in res:
            if val != prev:
                break
            ans[val].append(index)
            prev = val
        
        return ans[prev]
            






