from itertools import islice
class LRUCache:
    def __init__(self, capacity: int):
        self.storage = collections.deque()
        self.limit = capacity
        self.timer = 0

    def get(self, key: int) -> int:
        for i in range(len(self.storage)):
            if self.storage[i][0] == key:
                res = self.storage[i]
                new = list(islice(self.storage, 0, i)) + list(islice(self.storage, i + 1, len(self.storage)))
                self.storage = collections.deque(new)
                self.storage.append(res)
                return res[1]
        return -1

    def put(self, key: int, value: int) -> None:
        for i in range(len(self.storage)):
            if self.storage[i][0] == key:
                res = self.storage[i]
                new = list(islice(self.storage, 0, i)) + list(islice(self.storage, i + 1, len(self.storage)))
                self.storage = collections.deque(new)
                res[1] = value
                self.storage.append(res)
                return
            
        if len(self.storage) == self.limit:
            self.storage.popleft()

        self.storage.append([key, value])