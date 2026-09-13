class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        N = len(nums)
        l, r = 0, N - 1
        while l < r:
            S = nums[l] + nums[r]
            if S == target:
                return [l + 1, r + 1]
            
            if S > target:
                while r > l and nums[r] + nums[l] == S:
                    r -= 1
            else:
                while l < r and nums[l] + nums[r] == S:
                    l += 1
        return [-1, -1]