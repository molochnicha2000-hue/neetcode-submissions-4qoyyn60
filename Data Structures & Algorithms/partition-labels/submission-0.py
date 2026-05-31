class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        maps = collections.defaultdict(list)
        N = len(s)
        for i in range(N):
            maps[s[i]].append(i)

        actual = []
        for char, index in maps.items():
            actual.append([index[0], index[-1]])
        
        res = []
        N = len(actual)
        cur = actual[0]
        count = 0
        for i in range(1, N):
            new = actual[i]
            if cur[1] < new[0]:
                count = cur[1] - cur[0]
                res.append(count + 1)
                cur = new
            else:
                cur = [min(cur[0], new[0]), max(cur[1], new[1])]
                #count = cur[1] - cur[0]
        #print(actual, count)
        if cur:
            count = 1 + cur[1] - cur[0]
            res.append(count)
        return res