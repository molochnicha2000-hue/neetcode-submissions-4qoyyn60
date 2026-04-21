class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
    
    def addWord(self, word):
        root = self
        for c in word:
            if c not in root.children:
                root.children[c] = TrieNode()
            root = root.children[c]
        root.end = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        rows, cols = len(board), len(board[0])
        res, visit = set(), set()

        root = TrieNode()
        for word in words:
            root.addWord(word)

        def dfs(r, c, node, word):
            if (r < 0 or c < 0 or 
            r >= rows or c >= cols or 
            board[r][c] not in node.children or (r, c) in visit):
                return
    
            visit.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]

            if node.end:
                res.add(word)

            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)

            visit.remove((r, c))


        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root, "")
                    
        return list(res)

        