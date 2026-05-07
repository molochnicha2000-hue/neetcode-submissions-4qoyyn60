class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = float("-inf")
        stack = [] # (index, height)

        for i, h in enumerate(heights):
            start = i

            while stack and stack[-1][1] > h:
                cur_ind, cur_h = stack.pop()
                res = max(res, cur_h * (i - cur_ind))
                start = cur_ind

            stack.append((start, h))
            
            #print(stack)
        N = len(heights)
        for i, h in stack:
            res = max(res, (N - i) * h)
        return res