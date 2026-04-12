class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        if t == "":
            return ""

        need_have = {}
        for i in t:
            need_have[i] = 1 + need_have.get(i, 0)
        
        have, need = 0, len(need_have)
        len_res = float("inf")
        res = [-1, -1]
        l = 0
        window = {}
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)
            if c in need_have and window[c] == need_have[c]:
                have += 1
            print(window)
            while have == need:
                if (r - l + 1) < len_res:
                    res = [l, r]
                    len_res = (r - l + 1)
                
                window[s[l]] -= 1
                if s[l] in need_have and window[s[l]] < need_have[s[l]]:
                    have -= 1
                print(window)
                l += 1
        l, r = res
        return s[l: r + 1] if len_res != float("inf") else ""
