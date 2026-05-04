class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        daysDay = [1, 7, 30]
        dayCost = {
            costs[0]: 1,
            costs[1]: 7,
            costs[2]: 30
        }
        memo = {}
        def dfs(idx):
            if idx >= len(days):
                return 0
            if idx in memo:
                return memo[idx]

            res = float("inf")
            j = idx
            for i in range(3):
                while j < len(days) and days[j] < days[idx] + daysDay[i]:
                    j += 1
                res = min(res, costs[i] + dfs(j))
            memo[idx] = res
            return res
        return dfs(0) # ind of days 0
        
        
        