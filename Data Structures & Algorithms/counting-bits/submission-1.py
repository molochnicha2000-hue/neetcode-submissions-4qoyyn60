class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        pivot = 1
        for num in range(1, n + 1):
            if pivot * 2 == num:
                pivot = num
            dp[num] = (1 + dp[num - pivot])
        return dp
        