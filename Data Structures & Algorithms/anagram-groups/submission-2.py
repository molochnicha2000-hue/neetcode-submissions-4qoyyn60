class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = collections.defaultdict(list)

        for ch in strs:
            sort_ch = sorted(ch)
            anagrams["".join(sort_ch)].append(ch)
            #print(anagrams)
        
        res = []
        for i in anagrams:
            res.append(anagrams[i])
        return res

        
        