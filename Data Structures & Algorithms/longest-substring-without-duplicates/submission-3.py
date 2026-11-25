class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        f = Counter(); ans = 0; l = 0
        for r, x in enumerate(s):
            f[x] += 1
            while f[x] == 2:
                f[s[l]] -= 1
                l += 1
            ans = max(ans, r - l + 1)
        return ans