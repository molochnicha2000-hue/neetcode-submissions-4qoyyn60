class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        target = sum(nums) / k
        N = len(nums)

        used = [False] * N
        #cur = []
        def dfs(i, k, Sum):
            if k == 0:
                return True

            if Sum == target:
                return dfs(0, k - 1, 0)
                        

            for j in range(i, N):
                if used[j] or Sum + nums[j] > target:
                    continue          
                used[j] = True
                if dfs(j + 1, k, Sum + nums[j]):
                    return True
                used[j] = False
                if Sum == 0:
                    return False
            return False
        
        return dfs(0, k, 0)