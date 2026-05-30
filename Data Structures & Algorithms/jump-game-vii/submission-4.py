class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        if s[-1] == "1":
            return False
        N = len(s)
        dp = [False] * N
        dp[0] = True
        poss_steps = 0
        for i in range(1, N):
            if i >= minJump and dp[i - minJump]:
                poss_steps += 1
            
            if i > maxJump and dp[i - maxJump - 1]:
                poss_steps -= 1
            
            if s[i] == "0" and poss_steps > 0:
                dp[i] = True
        return dp[-1]