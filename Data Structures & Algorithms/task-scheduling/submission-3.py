class Solution:
    def leastInterval(self, tasks: List[str], k: int) -> int:
        n = len(tasks)
        f = collections.Counter(tasks)
        h = [-freq for freq in f.values()]
        heapq.heapify(h)
        q = collections.deque()
        time = 0
        while h or q:
            time += 1
            if h:
                cnt = 1 + heapq.heappop(h)
                if cnt < 0:
                    q.append((cnt, time + k))
            
            if q and q[0][1] == time:
                rem, _ = q.popleft()
                heapq.heappush(h, rem)
        return time