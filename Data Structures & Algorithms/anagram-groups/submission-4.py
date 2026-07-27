class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = collections.defaultdict(list)

        for w in strs:
            f = [0] * 26
            for c in w:
                f[ord(c) - ord('a')] += 1
            res[tuple(f)].append(w)
        
        ans = [cur for cur in res.values()]
        return ans