class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        todoList = {}
        for i in range(numCourses):
            todoList[i] = []

        for cur, need in prerequisites:
            todoList[cur].append(need)

        # return False if there is a loop
        visit = set()
        def dfs(cur):
            if cur in visit:
                return False

            if not todoList[cur]:
                return True
            
            visit.add(cur)
            for i in todoList[cur]:
                if not dfs(i):
                    return False
            
            visit.remove(cur)
            todoList[cur] = []
            return True
        
        for i in todoList:
            for j in todoList[i]:
                if not dfs(j):
                    return False
        return True