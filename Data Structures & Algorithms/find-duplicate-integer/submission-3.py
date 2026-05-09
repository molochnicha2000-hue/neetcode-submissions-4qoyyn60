class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # if I need to write my code in O(1) extra space
        # I need to use input array also all nums from 1 - N
        # [1, 2, 3, 2, 2]
        # []
        N = len(nums)

        for i in range(N):
            idx = abs(nums[i]) - 1
            #print(nums)
            if nums[idx] < 0:
                return abs(nums[i])
            nums[idx] *= -1

            #print(nums)
        return -1