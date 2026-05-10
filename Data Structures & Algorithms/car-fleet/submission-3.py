class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = [] # time
        # S = V * t
        # [1, 2, 3, 4] -> monotonic increasing. from the fastest to the worst
        # sort pos 
        pairs = [(p, s) for p, s in zip(position, speed)]
        pairs.sort(reverse = True)
        #print(pairs)
        for p, s in pairs:
            cur = (target - p) / s
            stack.append(cur)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                
                stack.pop()

        #print(stack)
        return len(stack)