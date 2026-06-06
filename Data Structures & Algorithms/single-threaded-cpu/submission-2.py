class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i, task in enumerate(tasks):
            task.append(i)
        tasks.sort(key = lambda x : x[0])
        minH = []     
        res = []
        i, time = 0, tasks[0][0]

        while minH or i < len(tasks):
            while i < len(tasks) and time >= tasks[i][0]:
                heapq.heappush(minH, (tasks[i][1], tasks[i][2]))
                i += 1
            if not minH:
                time = tasks[i][0]
            else:
                need, index = heapq.heappop(minH)
                res.append(index)
                time += need
        return res