class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l, r = max(nums), sum(nums)
        res = r
        def canSplit(largest):
            curSum = 0
            subArr = 0
            for n in nums:
                curSum += n
                if curSum > largest:
                    subArr += 1
                    curSum = n
            return subArr + 1 <= k
        # now we must be greedy
        while l <= r:
            mid = (l + r) // 2
            # if we can split arr on 2 s
            if canSplit(mid):
                r = mid - 1
                res = mid
            else:
                l = mid + 1                 
        return res