class LFUCache:
    def __init__(self, capacity: int):
        self.limit = capacity        
        self.storage = {}
        self.capacity = 0
        self.time = 0

    def get(self, key: int) -> int: 
        if key not in self.storage:
            return -1

        self.storage[key][1] += 1 # count
        value = self.storage[key][0]
        self.time += 1
        self.storage[key][2] = self.time # time
        return value

    def put(self, key: int, value: int) -> None:
        if self.limit <= 0:
            return

        self.time += 1
        if key in self.storage:
            self.storage[key][0] = value
            self.storage[key][1] += 1
            self.storage[key][2] = self.time
            return

        if len(self.storage) >= self.limit:
            min_freq = float("inf")
            min_time = float("inf")
            need = None
            for k, (val, freq, time) in self.storage.items():
                if freq < min_freq or (freq == min_freq and time < min_time):
                    min_freq = freq
                    min_time = time
                    need = k
            if need is not None:
                del self.storage[need]
        

        self.storage[key] = [value, 1, self.time]
        
# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)