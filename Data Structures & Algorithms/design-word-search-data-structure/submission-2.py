class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.end = True 
        

    def search(self, word: str) -> bool:
    
        resLen = len(word)
        cur = self.root
        def dfs(root, j):
            cur = root
            for i in range(j, len(word)):
                if word[i] == ".":
                    for child in cur.children.values():
                        if dfs(child, i + 1):
                            return True
                    return False
                else:
                    if word[i] not in cur.children:
                        return False
                    #if cur.end:
                        #return True
                    cur = cur.children[word[i]]
            return cur.end
        return dfs(cur, 0)
