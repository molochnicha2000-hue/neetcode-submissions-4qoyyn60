class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        N = len(nums)
        cur = []
        def dfs(i):
            # do subsets with len == k
            nonlocal res
            if i == N:
                res.append(cur.copy())
                return
            
            # we can include or no include
            cur.append(nums[i])
            dfs(i + 1)

            cur.pop()
            dfs(i + 1)
        dfs(0)
        return res


            
        