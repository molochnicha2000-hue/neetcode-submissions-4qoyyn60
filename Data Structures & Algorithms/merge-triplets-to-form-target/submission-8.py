class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        n = len(triplets)
        poss = []

        def good(cur) : return all(x <= y for x, y in zip(cur, target))
        for cur in triplets:
            if good(cur) : poss.append(cur)
        
        R = [False] * 3
        for cur in poss:
            for i in range(3):
                if cur[i] == target[i] : R[i] = True
        return all(R)


