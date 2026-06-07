class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        storage = {}
        for index, char in enumerate(order):
            storage[char] = index
        
        for i in range(len(words) - 1):
            first, second = words[i], words[i + 1]
            j = 0
            
            while j < min(len(first), len(second)) and first[j] == second[j]:
                j += 1

            if (j < min(len(first), len(second)) and 
                storage[first[j]] > storage[second[j]]):
                return False
            
            if j == min(len(first), len(second)) and len(first) > len(second):
                return False
            #print(j)
        return True 
        