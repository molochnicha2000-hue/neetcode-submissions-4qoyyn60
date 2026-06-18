class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0
        nums.sort()
        need_del = [] # indexs
        k = 0
        N = len(nums)
        start = float("-inf")
        for index, num in enumerate(nums):
            if num == val:
                start = index
                end = index + 1      
                while end < N and nums[end] == val:
                    end += 1
                break
        if start != float("-inf"):
            nums[::] = nums[:start] + nums[end : ]
        return len(nums)