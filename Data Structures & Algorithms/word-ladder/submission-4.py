class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList or beginWord == endWord:
            return 0
        
        def possible(curWord, potenWord):
            cur = 0
            for i in range(len(curWord)):
                if curWord[i] != potenWord[i]:
                    cur += 1
                if cur > 1:
                    return False
        
            return cur == 1
        
        q = collections.deque([(beginWord, 1)])
        visited = set(beginWord)

        while q:
            curWord, steps = q.popleft()
            if curWord == endWord:
                return steps
            
            for word in wordList:
                if word not in visited and possible(curWord, word):
                    visited.add(word)
                    q.append((word, steps + 1))
        return 0
        