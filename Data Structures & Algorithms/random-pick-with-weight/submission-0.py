class Solution:
    def __init__(self, w: List[int]):
        N = len(w)
        self.Summary = sum(w)
        self.heap = []
        self.count = None

        for index, val in enumerate(w):
            current = val / self.Summary
            heapq.heappush(self.heap, (-current, index))

    def pickIndex(self) -> int:
        prob, index = self.heap[0]
        return index
# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()