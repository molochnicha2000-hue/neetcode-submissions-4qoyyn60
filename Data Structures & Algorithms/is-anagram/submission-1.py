class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        f_dict = {}
        for c in s:
            f_dict[c] = 1 + f_dict.get(c, 0)

        for c in t:
            f_dict[c] = f_dict.get(c, 0) - 1

        for i in f_dict.values():
            if i != 0:
                return False
        return True
        
        