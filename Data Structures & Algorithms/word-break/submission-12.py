from functools import cache
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        N = len(wordDict)
        sw = set(wordDict)

        @cache
        def dfs(i):
            if i >= len(s):
                return True

            best = False
            word = ''
            for j in range(i, len(s)):
                word += s[j]
                if word in sw:
                    current = dfs(j + 1)
                    best |= current
            return best
        
        res = dfs(0)
        return res
