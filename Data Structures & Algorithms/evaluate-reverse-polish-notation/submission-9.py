class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        N = len(tokens)
        stack = []

        for x in tokens:
            if x not in '+/-*':
                stack.append(int(x))
                continue
            
            if x == '+':
                second = stack.pop()
                first = stack.pop()
                stack.append(second + first)

            elif x == '-':
                second = stack.pop()
                first = stack.pop()
                stack.append(first - second)

            elif x == '/':
                second = stack.pop()
                first = stack.pop()
                stack.append(int(first / second))

            else:
                second = stack.pop()
                first = stack.pop()
                stack.append(first * second)
        return stack[0]
