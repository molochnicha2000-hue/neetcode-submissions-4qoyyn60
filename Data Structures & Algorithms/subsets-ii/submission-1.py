class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        N = len(nums)

        cur = []
        def dfs(i):
            if i >= N:
                res.append(cur.copy())
                return
            
            res.append(cur.copy())

            prev = -21
            for j in range(i, N):
                if nums[j] == prev:
                    #print("yes")
                    continue
                
                cur.append(nums[j])
                dfs(j + 1)

                cur.pop()
                #dfs(j + 1)
                prev = nums[j]
            
        
        dfs(0)
        return res
        