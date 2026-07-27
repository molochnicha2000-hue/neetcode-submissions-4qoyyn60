from sortedcontainers import SortedList

class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        N = len(username)
        chron = collections.defaultdict(lambda : SortedList())
        
        for name, time, web in zip(username, timestamp, website):
            chron[name].add((time, web))

        patterns = collections.defaultdict(lambda : 0)

        for name in chron.keys():
            N = len(chron[name])
            s = set()
            for i in range(N):
                for j in range(i + 1, N):
                    for k in range(j + 1, N):
                        current = tuple([chron[name][i][1], chron[name][j][1], chron[name][k][1]])
                        s.add(current)
            for pat in s:
                patterns[pat] += 1

        res_pattern = None
        res_freq = 0
        for pat, freq in patterns.items():
            if not res_pattern:
                res_pattern = pat
                res_freq = freq
                continue
            #re = "".join([res_pattern[0][1], res_pattern[1][1], res_pattern[2][1]])
            #cu = "".join([pat[0][1], pat[1][1], pat[2][1]])
            if res_freq < freq or (res_freq == freq and res_pattern > pat):
                res_pattern = pat
                res_freq = freq
            
            # if res_freq == freq:
            #    res_pattern = min(res_pattern, pat)
        # print(res_pattern)
        res = list(res_pattern)
        return res