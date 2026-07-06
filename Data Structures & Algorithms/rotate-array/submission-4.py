class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        times = k % N
        if times == 0:
            return
        
        
        nums[::] = nums[N - times :] + nums[:N - times]