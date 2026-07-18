from sortedcontainers import SortedSet
class LFUCache:
    def __init__(self, capacity: int):
        self.storage = {}
        self.capacity = capacity
        self.time = 0

    def get(self, key: int) -> int:
        res = self.storage[key][0] if key in self.storage else -1

        if res != -1:
            self.storage[key][1] += 1
            self.time += 1
            self.storage[key][2] = self.time

        return res

    def put(self, key: int, value: int) -> None:
        if self.capacity <= 0:
            return

        self.time += 1
        if key in self.storage:
            self.storage[key][0] = value
            self.storage[key][1] += 1
            self.storage[key][2] = self.time
            return

        if len(self.storage) >= self.capacity:
            need_k = None
            MIN_used = float('inf')
            min_time = float('inf')

            for k, (val, used, recent_used) in self.storage.items():
                if used < MIN_used or (used == MIN_used and recent_used < min_time):
                    need_k = k
                    MIN_used = used
                    min_time = recent_used

            if need_k is not None:
                del self.storage[need_k]

        self.storage[key] = [value, 1, self.time]








# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)