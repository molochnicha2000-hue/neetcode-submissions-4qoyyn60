class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        n=len(nums)

        def f(i, current, arr):
            if current == target:
                ans.append(arr)
                return

            if current > target:
                return
            if i == n:
                return
            
            f(i+1, current, arr)
            f(i, current + nums[i], arr + [nums[i]])

        ans = []
        f(0, 0, [])
        return ans
