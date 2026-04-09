class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        first_dict = {}
        second_dict = {}
        
        for ch in s:
            if ch in first_dict:
                first_dict[ch] +=1
            else:
                first_dict[ch] = 0
        
        for ch in t:
            if ch in second_dict:
                second_dict[ch] +=1
            else:
                second_dict[ch] = 0

        return first_dict == second_dict 
        