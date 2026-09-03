from functools import cache
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        visit = set()
        q = collections.deque([(1, beginWord, 0)])
        while len(q) > 0:
            steps, w1, mask = q.popleft()
            if w1 == endWord:
                return steps
            if w1 in visit:
                continue
            visit.add(w1)
            for i, w2 in enumerate(wordList):
                if mask & (1 << i):
                    continue
                diff = 0
                for c1, c2 in zip(w1, w2):
                    if c1 != c2:
                        diff += 1

                if diff <= 1:
                    q.append((steps + 1, w2, mask | (1 << i)))
        return 0
                