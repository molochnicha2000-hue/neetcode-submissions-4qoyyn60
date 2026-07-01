class Solution:
    def numDecodings(self, s: str) -> int:
        N = len(s)
        dp = {}

        def dfs(index):
            if index == N:
                return 1
            
            if index in dp:
                return dp[index]
            
            char = s[index]
            best = dfs(index + 1) if char != "0" else 0
            if (index + 1 < N and (char == "1" 
                or char == "2" and s[index + 1] in "0123456")):
                best += dfs(index + 2) if index + 2 <= N else 0

            dp[index] = best
            return best

        res = dfs(0)
        
        return res
            