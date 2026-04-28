class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        N = len(temperatures)
        res = [0] * N
        for i in range(N):
            curr_t = temperatures[i]
            for j in range(i, N):
                if temperatures[j] > curr_t:
                    res[i] = j - i
                    break
        return res
        