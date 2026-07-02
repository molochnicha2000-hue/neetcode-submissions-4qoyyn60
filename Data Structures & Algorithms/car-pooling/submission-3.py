class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        N = len(trips)
        trips.sort(key = lambda x : x[1])
        heap = []
        for numPass, from_i, to_i in trips:
        
            while heap and heap[0][0] <= from_i:
                capacity += heap[0][1]
                heapq.heappop(heap)
            capacity -= numPass
            if capacity < 0:
                return False
            heapq.heappush(heap, (to_i, numPass))

        return True
