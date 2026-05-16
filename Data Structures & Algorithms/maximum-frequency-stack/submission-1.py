class FreqStack:

    def __init__(self):
        self.stack = {} # val -> freq
        self.realStack = []

    def push(self, val: int) -> None:
        self.stack[val] = 1 + self.stack.get(val, 0)
        self.realStack.append(val)

    def pop(self) -> int:
        freq = 0 # cur frequency
        resVal = -1
        #print(self.realStack, self.stack)

        for i in range(len(self.realStack) -1, -1, -1):
            cur = self.realStack[i]
            if freq < self.stack[cur]:
                resVal = cur
                freq = self.stack[cur]
                #print(cur, i)

        self.stack[resVal] -= 1
        
        flag = False
        for i in range(len(self.realStack) -1, -1, -1):
            if flag:
                break
            cur = self.realStack[i]
            if cur == resVal: 
                del self.realStack[i]
                flag = True

        return resVal


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()