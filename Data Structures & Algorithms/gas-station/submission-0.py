class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        N = len(gas)
        
        for i in range(N):
            tank = gas[i] - cost[i]
            if tank < 0:
                continue
            
            j = (i + 1) % N
            while j != i:
                tank += gas[j]
                tank -= cost[j]
                if tank < 0:
                    break
                
                j += 1
                j = j % N
            
            if j == i:
                return i
        return -1