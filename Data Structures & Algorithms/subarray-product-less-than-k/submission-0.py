class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        N = len(nums)
        l = 0
        current = 1
        res = 0
        for r in range(N):
            current *= nums[r]
            while l <= r and current >= k:
                current //= nums[l]
                l += 1
            if current < k:
                res += (r - l + 1)
        """
        10  5   2   6
            l       r            


        """
    
        return res
