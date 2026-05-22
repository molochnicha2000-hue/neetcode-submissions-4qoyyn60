class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        N = len(wordDict)
        targetLen = len(s)
        
        dp = {targetLen : True} 
        def dfs(i):
            if i in dp:
                return dp[i]

            for w in wordDict:
                if i + len(w) <= targetLen and s[i : i + len(w)] == w:
                    if dfs(i + len(w)):
                        return True

            dp[i] = False

        res = dfs(0)
        return res if res else False
        