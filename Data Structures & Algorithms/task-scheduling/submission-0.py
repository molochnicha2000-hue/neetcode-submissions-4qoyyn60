class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # only 26 chars(A - Z)
        N = len(tasks)
        heap = []
        q = collections.deque() # (repeats, waiting time)
        tasks_dict = {}
        for i in tasks:
            tasks_dict[i] = 1 + tasks_dict.get(i, 0)
        
        for ch, repeats in tasks_dict.items():
            heapq.heappush(heap, -repeats)
        
        time = 0
        while heap or q:
            time += 1
            if heap:
                cnt = 1 + heapq.heappop(heap)
                if cnt != 0:
                    q.append([cnt, time + n])
            
            if q and q[0][1] == time:
                cur = q.popleft()[0]
                heapq.heappush(heap, cur)
        

        return time
