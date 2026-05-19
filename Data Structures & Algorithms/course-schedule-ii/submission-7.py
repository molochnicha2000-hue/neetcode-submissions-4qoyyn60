class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
     
        graph = {i : [] for i in range(numCourses)}
        for u, v in prerequisites:
            graph[v].append(u)
        res = []
        visit, cycle = set(), set()
        # we want return if we reached empty
        def dfs(i):
            if i in cycle:
                return False

            if i in visit:
                return True

            cycle.add(i)
            for j in graph[i]:
                if not dfs(j):
                    return False
            cycle.remove(i)
            visit.add(i)
            res.append(i)
            return True 

        for i in range(numCourses):
            if not dfs(i):
                return []
        return res[::-1]