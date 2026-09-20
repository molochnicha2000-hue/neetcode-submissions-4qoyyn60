class Node:
    def __init__(self):
        self.child = {}
        self.end = False
class Trie:
    def __init__(self):
        self.root = Node()
    def add(self, w):
        cur = self.root
        for x in w:
            if x not in cur.child:
                cur.child[x] = Node()
            cur = cur.child[x]
        cur.end = True

    def search(self, w):
        q = collections.deque([(self.root, 0)])
        while len(q) > 0:
            node, i = q.popleft()
            if i == len(w):
                if node.end : return True
                continue

            if w[i] == '.':
                for ch in range(26):
                    char = chr(97 + ch)
                    if char in node.child:
                        q.append((node.child[char], i + 1))
            else:
                if w[i] in node.child:
                    q.append((node.child[w[i]], i + 1))
        return False
        

class WordDictionary:
    def __init__(self):
        self.tree = Trie()

    def addWord(self, word: str) -> None:
        self.tree.add(word)

    def search(self, word: str) -> bool:
        return self.tree.search(word)
