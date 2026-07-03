class MedianFinder:
    def __init__(self):
        self.Maxheap = []
        self.Minheap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.Maxheap, -num)
        if self.Minheap and self.Minheap[0] < num:
            current = -1 * heapq.heappop(self.Maxheap)
            heapq.heappush(self.Minheap, current)
        
        if len(self.Minheap) - len(self.Maxheap) > 1:
            current = heapq.heappop(self.Minheap)
            current *= (-1)
            heapq.heappush(self.Maxheap, current)
            
        elif len(self.Maxheap) - len(self.Minheap) > 1:
            current = heapq.heappop(self.Maxheap)
            current *= (-1)
            heapq.heappush(self.Minheap, current)

        #print(self.Minheap, self.Maxheap)
    def findMedian(self) -> float:
        if len(self.Maxheap) > len(self.Minheap):
            return (-1) * self.Maxheap[0]
        elif len(self.Minheap) > len(self.Maxheap):
            return self.Minheap[0]
        else:
            res = ((-1) * self.Maxheap[0] + self.Minheap[0]) / 2
            return res
        