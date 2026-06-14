class Solution:
    def reorganizeString(self, s: str) -> str:
        N = len(s)
        res = []
        a = {}
        for char in s:
            a[char] = 1 + a.get(char, 0)
        
        heap = [(-count, char) for char, count in a.items()]
        heapq.heapify(heap)
        
        while heap:
            count, char = heapq.heappop(heap)
            if res and char == res[-1]:
                if not heap:
                    return ""

                count2, char2 = heapq.heappop(heap)
                res += [char2]
                if count2 + 1 != 0:
                    heapq.heappush(heap, (count2 + 1, char2))
                heapq.heappush(heap, (count, char)) 
            else:
                res += [char]
                if count + 1 != 0:
                    heapq.heappush(heap, (count + 1, char))
        return "".join(res)