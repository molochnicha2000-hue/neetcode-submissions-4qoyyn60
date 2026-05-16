class StockSpanner:

    def __init__(self):
       self.stack = [] 

    def next(self, price: int) -> int:
        self.stack.append(price)
        N = len(self.stack)
        res = 0
        for i in range(N - 1, -1, -1):
            cur = self.stack[i]
            if cur > price:
                break
            
            res += 1
        return res
# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)