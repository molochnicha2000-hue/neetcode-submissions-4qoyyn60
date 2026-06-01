class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adg = collections.defaultdict(list)
        for from_i, to_i, weight in flights:
            adg[from_i].append((weight, to_i))
             
        #for from_i in adg:
            #adg[from_i].sort(key = lambda x: x[0])
        
        dp = {}
        def dfs(from_i, k):
            if from_i == dst:
                return 0
            
            if (from_i, k) in dp:
                return dp[(from_i, k)]

            if k < 0:
                return float("inf")
            best = float("inf")
            for weight, nei in adg[from_i]:
                best = min(best, dfs(nei, k - 1) + weight)

            dp[(from_i, k)] = best
            return dp[(from_i, k)]

        res = dfs(src, k)
        if res == float("inf"):
            return -1
        return res