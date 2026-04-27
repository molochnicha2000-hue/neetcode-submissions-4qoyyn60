class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums) < k:
            return [max(nums)]
        
        N = len(nums)
        l, r = 0, k - 1
        res = []
        """
        for r in range(N - k + 1, k):
            # [l: r + 1] == len(k)
            # after l = r
            res.append(max(nums[l: r + 1]))
            print(nums[l: r + 1], l, r)
            l = r
        """
        while r < N:
            res.append(max(nums[l:r + 1]))
            #print(nums[l: r + 1])
            l += 1
            r += 1
        return res