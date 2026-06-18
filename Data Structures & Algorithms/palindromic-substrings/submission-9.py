class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        N = len(s)

        def palindrome(l, r):
            res = 0
            while l >= 0 and r < N and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
            return res

        for i in range(N):
            l, r = i, i + 1
            res += palindrome(i, i + 1)

            l, r = i, i
            res += palindrome(i, i)
        return res