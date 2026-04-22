class MedianFinder:

    def __init__(self):
        self.storage = []
        

    def addNum(self, num: int) -> None:
        self.storage.append(num)

    def findMedian(self) -> float:
        self.storage.sort()
        storLen = len(self.storage)

        if storLen % 2 == 1:
            return self.storage[storLen // 2]
        else:
            return (self.storage[storLen // 2] + self.storage[storLen // 2 - 1]) / 2