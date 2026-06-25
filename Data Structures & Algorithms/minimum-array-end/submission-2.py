class Solution:
    def minEnd(self, N: int, x: int) -> int:
        res = x
        i = 1
        j = 1

        while j < N:
            if i & x == 0:
                if j & (N - 1):
                    res = res | i
                j = j << 1
            i = i << 1
        return res 
        

        