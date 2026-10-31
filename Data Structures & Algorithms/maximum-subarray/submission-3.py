class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        h = [0]; n = len(nums); ans = -math.inf; cur = 0
        for x in nums:
            cur += x
            ans = max(ans, cur - h[0])
            heapq.heappush(h, cur)
        return ans
        