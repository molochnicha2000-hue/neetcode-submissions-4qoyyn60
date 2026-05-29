class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        count = Counter(hand)
        hand.sort()

        for num in hand:
            if count[num]:
                for nxt in range(num, num + groupSize):
                    if not count[nxt]:
                        return False

                    count[nxt] -= 1
            
        return True 