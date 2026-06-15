class Solution:
    def calPoints(self, operations: List[str]) -> int:
        N = len(operations)
        stack = []
        """

        [1, 2, 3, 4]
        N = 3
        """
        visit = set()
        for i in range(N):
            cur = operations[i]
            if cur not in "+DC":
                stack.append(int(cur))
            elif cur == "+":
                stack.append(sum(stack[len(stack) - 2 : ]))

            elif cur == "D":
                stack.append(stack[-1] * 2)

            elif cur == "C":
                stack.pop()
        return sum(stack)
                