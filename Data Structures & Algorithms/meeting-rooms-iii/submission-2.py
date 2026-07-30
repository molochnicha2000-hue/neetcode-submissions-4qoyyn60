class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        f = collections.Counter()

        avail = [i for i in range(n)]
        heapq.heapify(avail)
        not_avail = []

        for i, (l, r) in enumerate(meetings):
            while len(not_avail) > 0 and not_avail[0][0] <= l:
                time, room = heapq.heappop(not_avail)
                heapq.heappush(avail, room)
            
            if len(avail) > 0:
                # print("YES", i)
                room = heapq.heappop(avail)
                f[room] += 1
                heapq.heappush(not_avail, (r, room))
                continue    
            
            # print(not_avail)
            delay = not_avail[0][0] - l
            # print(delay, i)
            time, room = heapq.heappop(not_avail)
            f[room] += 1
            heapq.heappush(not_avail, (delay + r, room))
        
        M = max(f.values())
        for room in sorted(f.keys()):
            if M == f[room]:
                return room

