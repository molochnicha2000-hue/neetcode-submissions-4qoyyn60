class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # if digit was before return it
        # all digits in the range of 1 - (N + 1)
        # range of 1 - N what does it give to me
        # 
        N = len(nums)
        visit = set()
        for n in range(N):
            if nums[n] in visit:
                return nums[n]
            else:
                visit.add(nums[n])
        return -1