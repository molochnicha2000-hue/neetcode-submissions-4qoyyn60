class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        L = []
        for x, y in points:
            L.append((math.sqrt(x ** 2 + y ** 2), [x, y]))
        L.sort(key = lambda x : x[0])
        return [L[i][1] for i in range(k)]
        