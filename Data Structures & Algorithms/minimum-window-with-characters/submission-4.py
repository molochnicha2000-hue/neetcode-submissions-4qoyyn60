class Solution:
    def minWindow(self, s: str, t: str) -> str:
        N = len(s)
        need = collections.Counter(t)
        f = collections.Counter()
        l = 0
        res = ''
        resLen = float('inf')
        for r in range(N):
            f[s[r]] += 1
            while l <= r and f[s[l]] > need[s[l]]:
                f[s[l]] -= 1
                if f[s[l]] == 0:
                    del f[s[l]]
                l += 1
            flag = True
            for char, freq in need.items():
                if f[char] < freq:
                    flag = False
                    break
            if flag:
                if resLen > r - l + 1:
                    res = s[l : r + 1]
                    resLen = r - l + 1
        return res