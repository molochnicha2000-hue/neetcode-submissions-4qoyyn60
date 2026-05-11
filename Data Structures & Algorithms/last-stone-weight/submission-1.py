class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        N = len(stones)
        res = []
        heap = []
        for i in range(N):
            heapq.heappush(heap, -stones[i])

        while heap and  len(heap) > 1:
            x, y = -1 * heapq.heappop(heap), -1 * heapq.heappop(heap)
            if x == y:
                continue
            elif y - x > 0:
                heapq.heappush(heap, -1 * (y - x))
            elif x - y > 0:
                heapq.heappush(heap, -1 * (x - y))
        return -1 * heap[0] if heap else 0
        