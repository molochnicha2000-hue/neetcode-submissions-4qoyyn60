class Solution:
    def largestRectangleArea(self, nums: List[int]) -> int:
        N = len(nums)
        res = 0
        stack = []
        for i, x in enumerate(nums):
            l = i
            while len(stack) > 0 and stack[-1][1] >= x:
                ind, val = stack.pop()
                res = max(res, val * (i - ind))
                l = ind
            stack.append((l, x))
        
        while len(stack) > 0:
            ind, val = stack.pop()
            res = max(res, val * (N - ind))
        return res