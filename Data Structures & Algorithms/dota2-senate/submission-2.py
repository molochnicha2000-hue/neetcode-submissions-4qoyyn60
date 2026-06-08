class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        N = len(senate)
        count_r = collections.deque()
        count_d = collections.deque()
        for i in range(N):
            if senate[i] == "R":
                count_r.append(i)
            else:
                count_d.append(i)

        while count_r and count_d:
            r = count_r.popleft()
            d = count_d.popleft()
            if r < d:
                count_r.append(r + N)
            else:
                count_d.append(d + N)
        
        return "Radiant" if count_r else "Dire"
            
            