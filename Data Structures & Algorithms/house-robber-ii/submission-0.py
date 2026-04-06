class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.robber(nums[1:]), self.robber(nums[:-1]))
    
    def robber(self, nums: List[int]) -> int:
        n1 = 0
        n2 = 0

        for n in nums:
            temp = max(n2, n1 + n)
            n1 = n2
            n2 = temp

        return n2