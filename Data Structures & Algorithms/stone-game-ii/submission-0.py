class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        N = len(piles)
        dp = {}
        # X - стопка
        def dfs(i, alice, M):
            if i >= N:
                return 0

            if (i, alice, M) in dp:
                return dp[(i, alice, M)]

            total = 0 
            best = 0 if alice else float("inf")
            for X in range(1, 2 * M + 1): 
                if i + X > N:
                    break
                total += piles[i + X - 1]
                if alice:
                    best = max(best, total + dfs(X + i, not alice, max(M, X)))
                else:
                    best = min(best, dfs(X + i, not alice, max(M, X)))
            dp[(i, alice, M)] = best
            return best

        return dfs(0, True, 1)

        """
                1  2 - 2
        alice - 4, 2, 5
        bob - 3,    3, 10
        """