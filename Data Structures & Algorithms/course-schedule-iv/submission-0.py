class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:   
        adg = {i : [] for i in range(numCourses)}

        for ai, bi in prerequisites:
            adg[ai].append(bi)

        
        def dfs(cur, target):
            if cur == target:
                return True
            
            if cur in visit:
                return False
            
            visit.add(cur)
            for nei in adg[cur]:
                if dfs(nei, target):
                    return True
            return False


        visit = set()
        res = []
        for ai, bi in queries:
            if dfs(ai, bi):
                res.append(True)
            else:
                res.append(False)
            visit.clear()
        return res