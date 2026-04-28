class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        N = len(temperatures)
        dp = [0] * N
        #dp[N - 1] = 0

        for i in range(N - 1, -1, -1):
            j = i + 1
            while j < N and temperatures[j] <= temperatures[i]:
                if dp[j] == 0:
                    j = N
                    break

                j += dp[j]
            print(dp)
            if j < N:
                dp[i] = j - i
        return dp
