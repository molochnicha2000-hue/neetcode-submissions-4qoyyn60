class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        N = len(nums)
        res = [0] * (N + 1)
        
        for i in range(N):
            res[nums[i]] += 1

        for i in range(N + 1):
            if res[i] == 0:
                return i
        
        return -1