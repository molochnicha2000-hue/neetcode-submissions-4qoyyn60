class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0
        
        # maybe sliding window
        cur = curLen = 0
        res = float("inf")
        l = 0
        N = len(nums)
        for r in range(N):
            cur += nums[r]
            curLen += 1
            while cur >= target:
                res = min(res, curLen)
                
                cur -= nums[l]
                curLen -= 1
                l += 1
        
        return res