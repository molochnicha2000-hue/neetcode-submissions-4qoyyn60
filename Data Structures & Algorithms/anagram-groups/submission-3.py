class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = collections.defaultdict(list)

        for s in strs:
            count = [0] * 26
            for ch in s:
                count[ord(ch) - ord("a")] += 1
            anagrams[tuple(count)].append(s)
        res = []
        for i in anagrams.values():
            res.append(i)
        return res

        
        
        

        

        