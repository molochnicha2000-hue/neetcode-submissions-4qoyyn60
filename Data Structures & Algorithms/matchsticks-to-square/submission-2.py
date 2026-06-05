class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total_length = sum(matchsticks)
        if total_length % 4 != 0:
            return False
        
        sides = total_length // 4
        square = [0] * 4
        N = len(matchsticks)
        matchsticks.sort(reverse = True)
        def dfs(i):
            if i == N:
                return True
            
            for side in range(4):
                if square[side] + matchsticks[i] <= sides:
                    square[side] += matchsticks[i]
                    if dfs(i + 1):
                        return True
                    square[side] -= matchsticks[i]
                if square[side] == 0:
                    break
            return False
        return dfs(0)