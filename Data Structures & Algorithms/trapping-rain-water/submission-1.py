class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        l, r = 0, len(height) - 1
        res = 0
        maxL, maxR = height[l], height[r]
        while l < r:    
            if maxL < maxR:
                l += 1
                maxL = max(maxL, height[l])
                if maxL - height[l] > 0:
                    res += maxL - height[l]
            else:
                r -= 1
                maxR = max(maxR, height[r])
                if maxR - height[r] > 0:
                    res += maxR - height[r]
        return res