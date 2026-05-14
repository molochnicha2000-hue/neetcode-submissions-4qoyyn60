class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #nums = list(set(nums))
        heap = []
        N = len(nums)

        for i in range(N):
            heapq.heappush(heap, -nums[i])
            #print(heap)
            if heap and N - k + 1 < len(heap):
                heapq.heappop(heap)
        #nums.sort()
        #print(nums)
        #print(heap)
        return -1 * heap[0]