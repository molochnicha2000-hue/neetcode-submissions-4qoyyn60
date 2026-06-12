class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        N = len(nums)
        for i in range(k % N):
            temp = nums[0]
            nums[0] = nums[-1]
            for j in range(1, N):
                nxt = nums[j]
                nums[j] = temp
                temp = nxt

            
         
        