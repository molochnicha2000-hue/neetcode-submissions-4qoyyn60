class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        N = len(piles)
        dp = {}
        def dfs(l, r):
            if l >= r:
                return 0

            if (l, r) in dp:
                return dp[(l, r)]

            even = True if (r - l) % 2 == 1 else False
            left = piles[l] if even else 0
            right = piles[r] if even else 0
            best = max(dfs(l + 1, r) + left, dfs(l, r - 1) + piles[r])

            dp[(l, r)] = best
            return best
        res = dfs(0, N - 1)
        #print(dp)
        return res > sum(piles) // 2