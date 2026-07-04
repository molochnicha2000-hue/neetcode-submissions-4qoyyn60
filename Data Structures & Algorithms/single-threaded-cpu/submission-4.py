class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        N = len(tasks)
        for i in range(N):
            tasks[i].append(i)
        tasks.sort(key = lambda x : x[0])
        res = []
        heap = []
        timer = tasks[0][0]
        i = 0
        while heap or i < N:
            while i < N and timer >= tasks[i][0]:
                heapq.heappush(heap, (tasks[i][1], tasks[i][2]))
                i += 1
            if not heap:
                timer = tasks[i][0]
            else:
                need, index = heapq.heappop(heap)
                res.append(index)
                timer += need

        return res