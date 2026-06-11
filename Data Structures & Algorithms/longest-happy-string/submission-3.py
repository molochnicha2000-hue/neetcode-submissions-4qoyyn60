class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = []
        if a:
            heapq.heappush(heap, (-a, "a"))
        if b:
            heapq.heappush(heap, (-b, "b"))
        if c:
            heapq.heappush(heap, (-c, "c"))
        res = ""


        while heap:
            amount, char = heapq.heappop(heap)

            if len(res) >= 2 and res[-1] == res[-2] == char:
                if not heap:
                    break
                
                amount1, char1 = heapq.heappop(heap)
                res += char1
                if amount1 + 1:
                    heapq.heappush(heap, (amount1 + 1, char1))
                heapq.heappush(heap, (amount, char))
                
            else:
                res += char
                if amount + 1:
                    heapq.heappush(heap, (amount + 1, char))
        return res