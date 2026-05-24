class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        rows, cols = len(word1), len(word2)

        dp = [[0] * (cols + 1) for _ in range(rows + 1)]

        for_r = rows
        for r in range(rows + 1):
            dp[r][-1] = for_r
            for_r -= 1

        for_c = cols
        for c in range(cols + 1):
            dp[-1][c] = for_c
            for_c -= 1
        
        dp[rows][cols] = 0
        for r in range(rows - 1, -1, -1):
            for c in range(cols - 1, -1, -1):
                if word1[r] == word2[c]:
                    dp[r][c] = dp[r + 1][c + 1]
                else:
                    dp[r][c] = 1 + min(dp[r + 1][c], dp[r][c + 1], dp[r + 1][c + 1])
        #print(dp)
        return dp[0][0] 