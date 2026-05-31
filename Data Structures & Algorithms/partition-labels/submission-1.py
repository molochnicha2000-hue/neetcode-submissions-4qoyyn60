class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        if s[0] == s[-1]:
            return [len(s)]
        N = len(s)
        maps = {s[i] : i for i in range(N)}
        #print(maps)
        res = []
        visit = set()
        for i in range(N):
            if s[i] in visit:
                continue
            size, end = 1, maps[s[i]]
            j = i + 1
            visit.add(s[i])
            while j < N and j <= end:
                visit.add(s[j])
                end = max(end, maps[s[j]])
                size += 1
                j += 1
            res.append(size)
        return res

        