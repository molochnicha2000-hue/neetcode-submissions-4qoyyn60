class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        N = len(people)
        people.sort()
        count = 0

        """
        1, 2, 4, 5
        1, 2, 2, 3, 3
        3, 3, 4, 5
        """
        
        l, r = 0, N - 1
        while l <= r:
        
            if people[r] + people[l] > limit:
                count += 1
                r -= 1
            #elif people[r] + people[l] < limit:
                #l += 1
            elif people[r] + people[l] <= limit:
                count += 1
                l += 1
                r -= 1
        return count