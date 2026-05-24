class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        N1, N2 = len(s1), len(s2)
        dp = [[False] * (N2 + 1) for i in range(N1 + 1)]
        dp[N1][N2] = True
        
        
        for r in range(N1, -1, -1): # s1
            for c in range(N2, -1, -1): # s2
                if r < N1 and s1[r] == s3[r + c] and dp[r + 1][c]:
                    dp[r][c] = True

                if c < N2 and s2[c] == s3[r + c] and dp[r][c + 1]:
                    dp[r][c] = True
    
                
        #print(dp)
        return dp[0][0]