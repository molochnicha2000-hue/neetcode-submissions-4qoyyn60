class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False


class PrefixTree:

    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:
        cur_root = self.root
        for c in word:
            if c not in cur_root.children:
                cur_root.children[c] = TrieNode()
            cur_root = cur_root.children[c]
        cur_root.endOfWord = True


    def search(self, word: str) -> bool:
        cur_root = self.root

        for c in word:
            if c not in cur_root.children: 
                return False
            cur_root = cur_root.children[c]
        return cur_root.endOfWord
        

    def startsWith(self, prefix: str) -> bool:
        cur_root = self.root

        for c in prefix:
            if c not in cur_root.children: 
                return False
            cur_root = cur_root.children[c]
        return True
        
        