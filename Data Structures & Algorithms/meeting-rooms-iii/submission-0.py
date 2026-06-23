class Solution:
    def mostBooked(self, N: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        count = [0] * N
        available = []

        for i in range(N):
            heapq.heappush(available, (0, i))
        
        for start, end in meetings:
            while available and available[0][0] < start:
                endT, room = heapq.heappop(available)
                heapq.heappush(available, (start, room))
            
            endT, room = heapq.heappop(available)
            heapq.heappush(available, (endT + (end - start), room))
            count[room] += 1
            
        return count.index(max(count))

        

