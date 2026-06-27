#from sortedcontainers import SortedList
class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        N = len(heights)
        stack = []

        for i in range(N):
            cur = heights[i]
            while stack and heights[stack[-1]] <= cur:
                stack.pop()
            stack.append(i)
        
        
        return stack