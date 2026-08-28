from functools import cache
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        N1, N2 = len(word1), len(word2)

        @cache
        def dfs(i, j):
            if j == N2:
                return N1 - i
            elif i == N1:
                return N2 - j
            
            if word1[i] != word2[j]:
                delete = dfs(i + 1, j)
                replace = dfs(i + 1, j + 1)
                insert = dfs(i, j + 1)
                return 1 + min(delete, replace, insert)    
            return dfs(i + 1, j + 1)
        return dfs(0, 0)