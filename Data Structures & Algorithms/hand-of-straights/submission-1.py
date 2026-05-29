class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        Hashmap = {}
        for num in hand:
            Hashmap[num] = 1 + Hashmap.get(num, 0)
        
        minH = list(Hashmap.keys())
        heapq.heapify(minH)
        
        while minH:
            first = minH[0]

            for i in range(first, first + groupSize):
                if not i in Hashmap:
                    return False
                
                Hashmap[i] -= 1
                if Hashmap[i] == 0:
                    #if i != minH[0]:
                        #print(i, minH[0])
                        #return False
                    heapq.heappop(minH)

        return True
        