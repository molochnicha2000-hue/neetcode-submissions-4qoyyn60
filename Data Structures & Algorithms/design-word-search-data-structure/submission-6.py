class TrieNode:
    def __init__(self):
        self.child = {}
        self.end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, w):
        cur = self.root
        for x in w:
            if x not in cur.child:
                cur.child[x] = TrieNode()
            cur = cur.child[x]
        cur.end = True

    def find(self, w):
        q = deque([(self.root, 0)])
        while len(q) > 0:
            cur, ind = q.popleft()
            if ind == len(w):
                if cur.end : return True
                continue
            if w[ind] == '.':
                for c in range(26):
                    char = chr(c + 97)
                    if char in cur.child:
                        q.append((cur.child[char], ind + 1))
            elif w[ind] in cur.child:
                q.append((cur.child[w[ind]], ind + 1))
        return False

class WordDictionary:
    def __init__(self):
        self.tree = Trie()

    def addWord(self, word: str) -> None:
        self.tree.add(word)

    def search(self, word: str) -> bool:
        return self.tree.find(word)
