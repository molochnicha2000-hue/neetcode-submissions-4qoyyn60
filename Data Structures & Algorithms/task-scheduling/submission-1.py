class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        N = len(tasks)
        q = collections.deque()
        heap = []
        f = collections.Counter(tasks)

        for char, freq in f.items():
            heapq.heappush(heap, -freq)
        
        res = 0
        while len(heap) > 0 or len(q) > 0:
            res += 1
            if len(heap) > 0:
                cnt = 1 + heapq.heappop(heap)
                if cnt != 0:
                    q.append((cnt, res + n))

            if len(q) > 0 and q[0][1] == res:
                cur = q.popleft()[0]
                heapq.heappush(heap, cur)
        return res
            