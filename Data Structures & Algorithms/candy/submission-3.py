class Solution:
    def candy(self, ratings: List[int]) -> int:
        N = len(ratings)
        res = [1] * N
        for i in range(1, N):
            if i - 1 >= 0 and ratings[i] > ratings[i - 1]:
                res[i] = res[i - 1] + 1

        for i in range(N - 1, -1, -1):
            if i + 1 < N and ratings[i] > ratings[i + 1]:
                if res[i] <= res[i + 1]:
                    res[i] = res[i + 1] + 1
 
        return sum(res)