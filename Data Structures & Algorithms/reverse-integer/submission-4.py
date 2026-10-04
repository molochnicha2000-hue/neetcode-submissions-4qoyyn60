class Solution:
    def reverse(self, x: int) -> int:
        sx = str(abs(x))
        R = (1 if x >= 0 else -1) * int(sx[::-1])
        
        if -(2 ** 31) <= R <= 2 ** 31 - 1 : return R
        return 0