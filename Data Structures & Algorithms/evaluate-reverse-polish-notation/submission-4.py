from math import ceil
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c not in "+-*/":
                stack.append(int(c))
            else:
                if c == "+":
                    x = stack.pop()
                    res = stack.pop()
                    stack.append(res + x)

                if c == "-":
                    x = stack.pop()
                    res = stack.pop()
                    stack.append(res - x)

                if c == "*":
                    x = stack.pop()
                    res = stack.pop()
                    stack.append(res * x)

                if c == "/":
                    x = stack.pop()
                    res = stack.pop()
                    stack.append(int(res / x))

        return int(stack[0])