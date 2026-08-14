class Solution:
    def decodeString(self, s: str) -> str:
        N = len(s)
        visit = set()
        def dfs(start):
            res = []
            for i in range(start, N):
                if i in visit:
                    continue

                visit.add(i)
                if s[i] == ']':
                    return res

                if s[i] in '123456789':
                    num = 0
                    while s[i] in '1234567890':
                        num = num * 10 + int(s[i])
                        visit.add(i)
                        i += 1
                    visit.add(i)
                    cur = num * dfs(i + 1)
                    # print(num, cur, s[i])
                    res += cur
                else:
                    res += s[i]
            return res
        r = dfs(0)
        return ''.join(r)