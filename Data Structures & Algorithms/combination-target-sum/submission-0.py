class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        cur = []
        N = len(nums)
        def backtrack(i):
            nonlocal res  
            if sum(cur) == target:
                res.append(cur.copy())
                return

            if sum(cur) > target or i >= N:
                return

            cur.append(nums[i])
            backtrack(i)

            cur.pop()
            backtrack(i + 1)

            
        backtrack(0)
        return res
        