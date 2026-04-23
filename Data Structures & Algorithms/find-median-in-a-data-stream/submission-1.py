class MedianFinder:
    def __init__(self):
        self.right = [] # big nums -> minHeap()
        self.left = [] # small nums -> maxHeap()

    def addNum(self, num: int) -> None:
        heapq.heappush(self.left, -num)

        if self.right and num > self.right[0]:
            val = heapq.heappop(self.left)
            heapq.heappush(self.right, -1 * val)

        if abs(len(self.left) - len(self.right)) > 1:
            if len(self.left) > len(self.right):
                val = -1 * heapq.heappop(self.left)
                heapq.heappush(self.right, val)

            if len(self.left) < len(self.right):
                val = heapq.heappop(self.right)
                heapq.heappush(self.left, -1 * val)

    def findMedian(self) -> float:
        if len(self.left) > len(self.right):
            return -1 * self.left[0]
        if len(self.left) < len(self.right):
            return self.right[0]
        return (-1 * self.left[0] + self.right[0]) / 2