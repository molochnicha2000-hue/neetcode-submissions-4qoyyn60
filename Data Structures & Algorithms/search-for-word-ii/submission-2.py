class TrieNode:
    def __init__(self):
        self.child = {}
        self.ind = None
class Solution:
    def findWords(self, grid: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for i, w in enumerate(words):
            cur = root
            for x in w:
                if x not in cur.child:
                    cur.child[x] = TrieNode()
                cur = cur.child[x]
            cur.ind = i
        
        m, n = len(grid), len(grid[0])
        d = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def dfs(r, c, node, visit):
            if node.ind is not None:
                ans.add(words[node.ind])
            
            for dr, dc in d:
                nr, nc = dr + r, dc + c
                if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visit:
                    ch = grid[nr][nc]
                    if ch in node.child:
                        dfs(nr, nc, node.child[ch], visit | {(nr, nc)})


        ans = set()
        for r in range(m):
            for c in range(n):
                if grid[r][c] in root.child:
                    dfs(r, c, root.child[grid[r][c]], {(r, c)})
        return list(ans)