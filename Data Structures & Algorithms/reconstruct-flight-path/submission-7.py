class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adg = defaultdict(list)
        tickets.sort(reverse = True)

        for from_i, to_i in tickets:
            adg[from_i].append(to_i)
        res = []
        def dfs(from_i):
            while adg[from_i]:
                cur = adg[from_i].pop()
                dfs(cur)
            
            res.append(from_i)
        dfs("JFK")
        return res[::-1]
        