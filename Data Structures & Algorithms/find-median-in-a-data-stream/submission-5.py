class MedianFinder:

    def __init__(self):
        self.minHeap = [] # [4, 5]
        self.maxHeap = [] # [1, 2, 3]

    def addNum(self, num: int) -> None:
        # bigger val and less val 
        heapq.heappush(self.maxHeap, -num)
        if self.minHeap and num > self.minHeap[0]:
            val = -1 * heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, val)


        # add minHeap[4, 5]
        if len(self.maxHeap) - 1 > len(self.minHeap):
            val = -1 * heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, val)

        # add maxHeap[1, 2, 3]
        if len(self.maxHeap) < len(self.minHeap) - 1: 
            val = -1 * heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, val)

        # so prob in if statements
        print(self.minHeap, self.maxHeap) # [1, 2] and [3]

    def findMedian(self) -> float:
        if len(self.minHeap) > len(self.maxHeap):
            return self.minHeap[0]
             
        if len(self.minHeap) == len(self.maxHeap):
            return (self.minHeap[0] + -1 * self.maxHeap[0]) / 2

        if len(self.minHeap) < len(self.maxHeap):
            return -1 * self.maxHeap[0]
            
        

        