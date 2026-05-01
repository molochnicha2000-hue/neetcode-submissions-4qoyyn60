class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        count = 0      
        pair = sorted(zip(position, speed), reverse = True)
        stack = []
        for p, s in pair:
            time = (target - p) / s
            stack.append(time)

            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                count += 1
                stack.pop()
        #print(stack)       
        return len(stack)