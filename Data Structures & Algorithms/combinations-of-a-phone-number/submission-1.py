class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        res = []
        cur = []
        N = len(digits)
        def dfs(i):
            if len(cur) == N:
                res.append(''.join(cur))
                return
            
            
            for h in letters[digits[i]]:
                cur.append(h)
                dfs(i + 1)

                cur.pop()
        dfs(0)
        return res
        