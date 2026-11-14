class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        nums.sort()

        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1] : continue
            mid = nums[i]
            l, r = i + 1, n - 1
            while l < r:
                left, right = nums[l], nums[r]
                S = left + mid + right
                if S == 0:
                    ans.append([left, mid, right])
                    while l < r and nums[l] == left:
                        l += 1
                elif S > 0:
                    r -= 1
                else:
                    l += 1
        return ans