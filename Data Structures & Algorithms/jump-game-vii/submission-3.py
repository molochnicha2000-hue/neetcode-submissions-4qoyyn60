class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        # I can move from i -> j if
        #   (i + minJump <= j <= min(i + maxJump, N - 1) and s[j] == "0")
        if s[0] == "1" or s[-1] == "1":
            return False
        N = len(s)
        dp = [False] * (N)
        dp[-1] = True
        for i in range(N - 1, -1, -1):
            cur = s[i]
            if cur == "1":
                continue
            for k in range(minJump, maxJump + 1):
                if i + k >= N:
                    break

                dp[i] = dp[i + k]

                if dp[i]:
                    break

        #print(dp)
        return dp[0]
        