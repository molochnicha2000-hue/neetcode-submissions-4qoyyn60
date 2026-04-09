class Solution:      
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # edge cases
        if not strs:
            return [['']]
        if len(strs) == 1:
            return [[strs[0]]]

        res = {}
        for string in strs:
            key = "".join(sorted(string))

            if key not in res:
                res[key] = []
            
            res[key].append(string)
            

        return list(res.values())
"""
    def getDict(self, string: str) -> dict:
        res = {}
        for char in string:
            if char in res:
                res[char] +=1
            else:
                res[char] = 0
        return res
"""
    