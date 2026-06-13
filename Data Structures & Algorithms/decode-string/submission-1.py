class Solution:
    def decodeString(self, s: str) -> str:
        N = len(s)
        """
        "2[a3[b]]c"
        visit
        """
        def dfs(i, visit):
            res = ""
            
            for j in range(i, N):
                if j in visit:
                    continue
                visit.add(j)
                if s[j] == "]":
                    return res

                if s[j] not in "123456789":
                    res += s[j]           
                else:
                    times = ""
                    i = j
                    while i < N and s[i] in "0123456789":
                        times += s[i]
                        visit.add(i)
                        i += 1

                    cur = dfs(i + 1, visit)
                    res += int(times) * cur
                    visit.add(i)
                    
            return res
        visit = set()
        res = dfs(0, visit)
        
        return res