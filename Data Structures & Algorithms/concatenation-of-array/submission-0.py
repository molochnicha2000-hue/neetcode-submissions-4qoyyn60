class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        N = len(nums)

        ans = [None] * (2 * N)

        for i in range(N):
            ans[i] = nums[i]
            ans[i + N] = nums[i]
        
        return ans
        