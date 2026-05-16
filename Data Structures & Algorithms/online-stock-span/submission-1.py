class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        #self.stack.append((price, 1))
        ind = 1
        while self.stack and self.stack[-1][0] <= price:
            ind += self.stack[-1][1]
            self.stack.pop()
        
        self.stack.append((price, ind))
        #print(self.stack, ind)
        return ind


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)