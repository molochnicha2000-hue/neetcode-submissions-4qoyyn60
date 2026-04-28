class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        output = [0] * len(temperatures)
        for i in range(len(temperatures)):
            while stack and temperatures[i] > stack[-1][0]:
                #stack.pop()
                #output.append(abs(i - stack[-1][1]))
                temp, day = stack[-1]
                output[day] = abs(i - stack[-1][1])     # j - place in temperat. 
                stack.pop()
            stack.append((temperatures[i], i))
        return output