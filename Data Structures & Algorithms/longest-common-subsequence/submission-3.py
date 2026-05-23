class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if text1 == text2:
            return len(text1)
        
        if len(text1) > len(text2):
            text1, text2 = text2, text1
        
        dp = {}
        def dfs(first, second): # first is lesser then second
            if not first or not second:
                return 0

            if (first, second) in dp:
                return dp[(first, second)]

            res = max(dfs(first, second[1:]), dfs(first[1:], second))

            if first[0] == second[0]:
                res = max(res, dfs(first[1:], second[1:]) + 1)

            dp[(first, second)] = res         
            return res
        
        return dfs(text1, text2)
        