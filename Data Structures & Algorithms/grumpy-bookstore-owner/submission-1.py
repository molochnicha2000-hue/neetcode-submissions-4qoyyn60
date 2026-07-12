class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        N = len(customers)
        res = 0
        good = 0
        current = 0
        l = 0
        for r in range(N):
            if grumpy[r]:
                current += customers[r]
            else:
                good += customers[r]
            
            if r - l + 1 > minutes:
                if grumpy[l]:
                    current -= customers[l]
                l += 1
            res = max(res, current)
        return good + res




