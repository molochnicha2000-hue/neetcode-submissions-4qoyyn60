class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        N = len(fruits)
        
        res = 0
        for i in range(N):
            total = 1
            first = fruits[i]
            second = None
            for j in range(i + 1, N):
                if (second and fruits[j] != second) and fruits[j] != first:
                    break

                if not second and fruits[j] != first:
                    second = fruits[j]

                total += 1

            res = max(res, total)
        return res