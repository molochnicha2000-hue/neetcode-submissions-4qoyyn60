class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        N = len(nums)
        heap = []
        for n in nums:
            heapq.heappush(heap, n)

        #print(heap)
        res = []
        for _ in range(N):
            cur = heapq.heappop(heap)
            res.append(cur)
        return res