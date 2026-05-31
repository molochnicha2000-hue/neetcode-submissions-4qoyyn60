class Solution:
    def checkValidString(self, s: str) -> bool:
        N = len(s)
        dp = {}

        def dfs(i, balance):
            if balance < 0 or i > N:
                return False
            if i == N:
                return balance == 0
            
            if (i, balance) in dp:
                return dp[(i, balance)]

            res = False
            if s[i] == "*":
                res = (dfs(i + 1, balance) or 
                    dfs(i + 1, balance - 1) or
                    dfs(i + 1, balance + 1))
            else:
                if s[i] == "(":
                    temp = 1
                else:
                    temp = -1
                res = dfs(i + 1, balance + temp)
                
            dp[(i, balance)] = res
            return res
        res = dfs(0, 0)
        return res