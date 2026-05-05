class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        N = len(gas)
        diff = [0] * N
        count = 0
        for i in range(N):
            diff[i] = gas[i] - cost[i]
            if diff[i] < 0:
                count += 1

        if count == N:
            return -1

        for i in range(N):
            total = diff[i]
            j = (i + 1) % N
            while total >= 0 and j != i:
                total += diff[j]
                if total < 0:
                    break
                j += 1
                j %= N
            if j == i:
                return i 
        return -1