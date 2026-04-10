from heapq import heappop, heappush
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for n in nums:
            counter[n] = 1 + counter.get(n, 0)
        
        minHeap = []
        for val, ti in counter.items():
            heapq.heappush(minHeap, (ti, val))

            if len(minHeap) > k:
                heapq.heappop(minHeap)
        
        k_freq_items = []
        while minHeap:
            k_freq_items.append(heappop(minHeap)[1])
        
        return k_freq_items