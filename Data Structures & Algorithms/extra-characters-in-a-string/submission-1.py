class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        N = len(s)
        dp = {}
        dictionary = set(dictionary)
        def dfs(i):
            if i >= N:
                return 0
            
            if i in dp:
                return dp[i]

            best = 1 + dfs(i + 1)
            for j in range(i, N):
                word = s[i : j + 1]
                if word in dictionary:
                    best = min(best, dfs(j + 1))
                
                
            dp[i] = best
            return best
        res = dfs(0)
        return res

