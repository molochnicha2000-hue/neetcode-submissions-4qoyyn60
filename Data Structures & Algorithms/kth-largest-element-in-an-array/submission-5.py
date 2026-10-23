class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        count = [0] * 2001
        for x in nums:
            count[x + 1000] += 1

        for i in range(2000, -1, -1):
            k -= count[i]
            if k <= 0:
                return i - 1000