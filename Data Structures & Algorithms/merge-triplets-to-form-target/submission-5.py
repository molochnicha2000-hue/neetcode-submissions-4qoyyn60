class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        N = len(triplets)

        deadend = set()
        possible = []
        for i in range(N):
            cur = triplets[i]
            for j in range(3):
                if cur[j] > target[j] and cur[j] != target[j]:
                    deadend.add(tuple(cur))
                    break
            if tuple(cur) not in deadend:
                possible.append(cur)

        
        res = [0] * 3
        for i in range(len(possible)):
            cur = possible[i]
            for k in range(3):
                if cur[k] == target[k]:
                    res[k] = cur[k]
        #print(res)
        return res == target