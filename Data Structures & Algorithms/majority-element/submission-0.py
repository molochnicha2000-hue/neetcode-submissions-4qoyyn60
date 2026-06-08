class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        N = len(nums)
        count = 0
        prev = nums[0]
        for i in range(1, N):
            if count == N // 2:
                return prev

            if prev == nums[i]:
                count += 1
            else:
                prev = nums[i]
        return prev            