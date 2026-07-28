class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        first = nums[n-k:]
        second = nums[:n-k]
        print(first + second)
        nums[::] = first + second
        # return second + first
        