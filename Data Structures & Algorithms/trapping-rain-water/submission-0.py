class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        maxL = [0] * len(height)
        maxR = [0] * len(height)

        curr_max = 0
        for i, n in enumerate(height):
            maxL[i] = curr_max
            if n > curr_max:
                curr_max = n

        curr_max = 0
        for i in range(len(height) -1, -1, -1):
            maxR[i] = curr_max
            if height[i] > curr_max:
                curr_max = height[i]

        for i in range(len(height)):
            curr = min(maxL[i], maxR[i]) - height[i]
            if curr > 0: 
                res += curr
        return res