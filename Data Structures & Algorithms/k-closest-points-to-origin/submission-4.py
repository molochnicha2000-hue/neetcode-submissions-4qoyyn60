import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        
        for i in range(len(points)):
            val1, val2 = points[i]
            curr_num = abs(val1) ** 2 + abs(val2)**2
            #heapq.heappush(minHeap, (curr_num, [val1,val2]))
            minHeap.append([curr_num, val1, val2])

            #if len(minHeap) > k:
                #minHeap.pop()
        res = []
        heapq.heapify(minHeap)
        while k > 0:
            dist, x, y = heapq.heappop(minHeap)
            res.append([x, y])
            k -= 1
            

        return res
        