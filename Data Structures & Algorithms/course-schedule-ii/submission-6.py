class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:     
        graph = {i : [] for i in range(numCourses)}
        for u, v in prerequisites:
            graph[u].append(v)
        res = []
        visit, cycle = set(), set()

        def dfs(i):
            if i in cycle:
                return False
            
            if i in visit:
                return True
            
            cycle.add(i)
            for nei in graph[i]:
                if not dfs(nei):
                    return False
                
            cycle.remove(i)
            visit.add(i)
            res.append(i)
            return True
        
        for c in range(numCourses):
            if not dfs(c): 
                return []
        return res
