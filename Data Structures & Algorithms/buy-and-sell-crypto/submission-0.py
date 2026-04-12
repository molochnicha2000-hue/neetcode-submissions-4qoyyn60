class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        l, r = 0, 1
        while r in range(len(prices)):
            if prices[r] - prices[l] > res:
                res = prices[r] - prices[l] 
            print("left",l)
            print("right",r)
            if prices[l] > prices[r]:
                l += 1
            else:
                r += 1
        return res