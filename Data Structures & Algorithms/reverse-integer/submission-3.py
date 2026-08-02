class Solution:
    def reverse(self, x: int) -> int:
        limits = [-pow(2, 31), pow(2, 31) - 1]
        
        ans = 0
        negative = False
        if x < 0:
            negative = True

        sx = str(abs(x))
        for num in reversed(sx):
            if ans * 10 + int(num) >= limits[1]:
                return 0
            ans *= 10
            ans += int(num)

        if negative:
            return -ans
        return ans