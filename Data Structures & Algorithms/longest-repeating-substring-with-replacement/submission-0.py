class Solution:
    def characterReplacement(self, s: str, k: int) -> int: 
        res = 0
        l = 0

        window = {}
        for r in range(len(s)):
            window[s[r]] = 1 + window.get(s[r], 0)
            curr_req = max(window.values())

            while (r - l + 1) - curr_req > k:
                window[s[l]] = window[s[l]] - 1
                l += 1
            
            res = max(res, (r - l + 1))
            
                
        return res
        