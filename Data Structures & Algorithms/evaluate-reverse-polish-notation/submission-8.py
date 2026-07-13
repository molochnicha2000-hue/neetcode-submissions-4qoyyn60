class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        N = len(tokens)
        res = 0
        stack = []

        for i in range(N):
            current = tokens[i]
            if current in "+-*/":
                if current == "+":
                    n = stack.pop() + stack.pop()
                    stack.append(n)

                if current == "-":
                    first = stack.pop()
                    second = stack.pop()
                    stack.append(second - first)

                if current == "*":
                    n = stack.pop() * stack.pop()
                    stack.append(n)

                if current == "/":
                    first = stack.pop()
                    second = stack.pop()
                    stack.append(int(second / first))
            else:
                stack.append(int(current))

        return stack[0]