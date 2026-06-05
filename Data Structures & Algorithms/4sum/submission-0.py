class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        N = len(nums)
        res = []
        """
        -3, 0, 1, 2, 3, 3
        """
        cur = []
        def dfs(k, need, start): 
            nonlocal res
            if k != 2:
                for j in range(start, N - k + 1):
                    if j > start and nums[j] == nums[j - 1]:
                        continue
                    cur.append(nums[j])
                    dfs(k - 1, need - nums[j], j + 1)

                    cur.pop()
                return

            l, r = start, N - 1
            while l < r:
                if nums[l] + nums[r] > need:
                    r -= 1
                elif nums[l] + nums[r] < need:
                    l += 1
                else:
                    res.append(cur + [nums[l]] + [nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
            
        dfs(4, target, 0)
        return res

            