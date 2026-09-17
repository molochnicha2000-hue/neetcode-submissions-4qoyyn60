class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        N = len(nums)
        l, r = 0, N - 1
        while l < r:
            S = nums[l] + nums[r]
            if S == target : return [l + 1, r + 1]
            if S < target : l += 1
            if S > target : r -= 1
        return [-1, -1]