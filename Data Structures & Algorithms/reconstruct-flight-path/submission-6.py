class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adg = {}
        for from_i, to_i in tickets:
            adg[from_i] = []
            
        tickets.sort()
        for from_i, to_i in tickets:
            adg[from_i].append(to_i)
            
        
        res = ["JFK"]
        N = len(tickets)
        def dfs(from_i):
            if len(res) == N + 1:
                return True
            
            if from_i not in adg:
                return False
            
            temp = list(adg[from_i])
            for i, to_i in enumerate(temp):
                adg[from_i].pop(i)
                res.append(to_i)

                if dfs(to_i):
                    return True
                
                adg[from_i].insert(i, to_i)
                res.pop()
            return False
        dfs("JFK")
        return res