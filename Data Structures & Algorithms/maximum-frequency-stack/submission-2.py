class FreqStack:

    def __init__(self):
        self.hashmap = {} # store Freq of val
        self.stack = collections.defaultdict(list) # store val by their frequency
        self.maxFreq = 0

    def push(self, val: int) -> None:
        self.hashmap[val] = 1 + self.hashmap.get(val, 0)
        cur = self.hashmap[val] # cur is freq of val
        self.stack[cur].append(val)

        self.maxFreq = max(self.maxFreq, cur)

    def pop(self) -> int:
        while self.maxFreq != 0 and not self.stack[self.maxFreq]:
            self.maxFreq -= 1
        res = self.stack[self.maxFreq].pop()
        self.hashmap[res] -= 1

        return res


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()