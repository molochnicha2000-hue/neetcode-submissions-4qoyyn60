class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        heapq.heapify(nums)

        res = []
        while len(nums) > 0:
            val = heapq.heappop(nums)
            res.append(val)
        return res