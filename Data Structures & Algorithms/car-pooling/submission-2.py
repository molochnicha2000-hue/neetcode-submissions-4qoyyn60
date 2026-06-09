import sortedcontainers
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        N = len(trips)
        trips.sort(key = lambda x : x[1])

        drop = sortedcontainers.SortedList()
        count = 0

        
        for cur in trips:
            passeng, from_i, to_i = cur

            while drop and drop[0][0] <= from_i:
                count -= drop[0][1]
                drop.pop(0)

            count += passeng
            if count > capacity:
                return False
            
            drop.add((to_i, passeng))

        return True