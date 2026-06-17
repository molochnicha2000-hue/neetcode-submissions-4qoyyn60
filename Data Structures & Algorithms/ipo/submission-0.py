class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        proj = sorted(zip(capital, profits))
        heap = []
        N = len(profits)
        i = 0
        for _ in range(k):
            
            while i < N and proj[i][0] <= w:
                heapq.heappush(heap, -proj[i][1])
                i += 1
            
            if not heap:
                break
            
            w += -heapq.heappop(heap)
        return w