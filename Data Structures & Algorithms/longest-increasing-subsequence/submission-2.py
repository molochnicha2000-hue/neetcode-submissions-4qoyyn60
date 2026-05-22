class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        N = len(nums)
        dp = {i : 1 for i in range(N)}

        for i in range(N - 1, -1, -1):       
            j = i
            while j < N :
                if nums[j] > nums[i]:
                    dp[i] = max(dp[i], 1 + dp[j])
                j += 1 
        
        res = 1
        for i, n in dp.items():
            res = max(res, n)
        print(dp)
        return res