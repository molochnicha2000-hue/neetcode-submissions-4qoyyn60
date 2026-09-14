class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        N = len(s)
        l = 0
        res = 0
        f = collections.Counter()
        for r, x in enumerate(s):
            f[x] += 1
            while f[x] > 1:
                f[s[l]] -= 1
                if f[s[l]] == 0:
                    del f[s[l]]
                l += 1
            res = max(res, r - l + 1)
        return res