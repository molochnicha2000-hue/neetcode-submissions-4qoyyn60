class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        cur = []
        
        def dfs(opened, closed):
            if opened == n and closed == n:
                res.append("".join(cur.copy()))
                return
            
            if opened > n or closed > n:
                return

            if opened < n:
                cur.append("(")
                dfs(opened + 1, closed)
                cur.pop()

            if closed < opened:
                cur.append(")")
                dfs(opened, closed + 1)
                cur.pop()

            #cur.pop()
            #dfs(opened, closed)

        dfs(0, 0)
        return res