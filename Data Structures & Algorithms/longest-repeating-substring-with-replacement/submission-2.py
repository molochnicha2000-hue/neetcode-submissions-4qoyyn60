class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        N = len(s)
        res = 0 

        for c in set(s):
            l, count = 0, 0
            for r in range(N):
                if s[r] != c:
                    count += 1
                
                while count > k:
                    if s[l] != c:
                        count -= 1
                    l += 1
                res = max(res, (r - l + 1))
        return res
                    
                    
