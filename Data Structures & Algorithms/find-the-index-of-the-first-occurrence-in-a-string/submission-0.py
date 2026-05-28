class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle in haystack:
            return -1
        res = None
        need = len(needle)
        N = len(haystack)
        for i in range(N):
            if haystack[i] == needle[0]:
                j = i
                cur = 0
                while j < N and cur < need and haystack[j] == needle[cur]:
                    j += 1
                    cur += 1
                if cur == need:
                    return i
        return -1