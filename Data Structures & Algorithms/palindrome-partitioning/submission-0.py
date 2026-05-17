class Solution:
    def check(self, cur):
        l, r = 0, len(cur) - 1
        N = len(cur)
        if N % 2 == 1:
            while l <= r:
                if cur[l] != cur[r]:
                    return False
                l += 1
                r -= 1
        else:
            while l < r:
                if cur[l] != cur[r]:
                    return False

                l += 1
                r -= 1
        return True 

    def partition(self, s: str) -> List[List[str]]:
        res = []
        cur = []
        N = len(s)
        def dfs(i):
            if i == N:
                res.append(cur.copy())
                return
                
            for j in range(i, N):
                if self.check(s[i : j + 1]):
                    cur.append(s[i : j + 1])
                    dfs(j + 1)

                    cur.pop() 
        dfs(0)
        return res