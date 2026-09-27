class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        f = collections.defaultdict(list)
        for x in strs:
            group = [0] * 26
            for y in x:
                group[ord(y) - 97] += 1
            f[tuple(group)].append(x)

        return [x for x in f.values()]