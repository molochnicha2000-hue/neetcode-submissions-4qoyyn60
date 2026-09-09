class TrieNode:
    def __init__(self):
        self.child = {}
        self.end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    def add(self, w):
        cur = self.root
        for c in w:
            if c not in cur.child:
                cur.child[c] = TrieNode()
            cur = cur.child[c]
        cur.end = True

    def search(self, s):
        N = len(s)
        q = collections.deque([(-1, self.root)])
        while len(q) > 0:
            ind, cur = q.popleft()
            if ind == N - 1:
                if cur.end:
                    return True
                continue
            if ind + 1 < N and s[ind + 1] in cur.child:
                q.append((ind + 1, cur.child[s[ind + 1]]))

            if ind + 1 < N and s[ind + 1] == '.':
                for i in range(26):
                    char = chr(i + 97)
                    if char in cur.child:
                        q.append((ind + 1, cur.child[char]))
        return False

class WordDictionary:
    def __init__(self):
        self.storage = Trie()

    def addWord(self, word: str) -> None:
        self.storage.add(word)

    def search(self, word: str) -> bool:
        return self.storage.search(word)
