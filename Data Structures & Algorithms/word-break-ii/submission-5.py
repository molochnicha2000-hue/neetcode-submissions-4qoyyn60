class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        N = len(s)
        res = []
        wordDict = set(wordDict)
        def dfs(i, c):
            nonlocal res
            if i == N:
                res.append(" ".join(c))
                return
            
            for j in range(i, N):
                w = s[i : j + 1]
                if w in wordDict:
                    dfs(j + 1, c + [w])
        
        dfs(0, [])
        return res



