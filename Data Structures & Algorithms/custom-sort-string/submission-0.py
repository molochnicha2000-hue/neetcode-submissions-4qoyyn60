class Solution:
    def customSortString(self, order: str, s: str) -> str:
        N = len(s)
        heap = []
        for char in s:
            default = float("inf")
            if char in order:
                default = order.index(char)        
            heapq.heappush(heap, (default, char))

        res = ""
        while len(heap) > 0:
            _, char = heapq.heappop(heap)
            res += char
        return res
       


        