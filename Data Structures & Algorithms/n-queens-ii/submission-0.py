class Solution:
    def totalNQueens(self, n: int) -> int:
        res = 0
        posD = set()
        negD = set()
        col = set()
        row = set()
        """

        ['.', '.', '.', '.'] n
        ['.', 'Q', '.', '.'] can
        ['.', '.', '.', '.']
        ['Q', '.', '.', '.']
          n   can

        """
        def dfs(r):
            nonlocal res
            if r == n:
                res += 1
                return

            for c in range(n):
                if (r + c) in posD or (r - c) in negD or c in col:
                    continue

                posD.add((r + c))
                negD.add((r - c))
                col.add(c)

                dfs(r + 1)

                posD.remove((r + c))
                negD.remove((r - c))
                col.remove(c)
        dfs(0)
        return res
