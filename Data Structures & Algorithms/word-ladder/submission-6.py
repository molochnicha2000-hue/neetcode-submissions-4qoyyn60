class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:   
        if endWord not in wordList:
            return 0
        
        graph = collections.defaultdict(list)

        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j + 1:]
                graph[pattern].append(word)
            
        visit = set([beginWord])
        q = collections.deque([beginWord])
        res = 1

        while q:
            for i in range(len(q)):
                curWord = q.popleft()
                if curWord == endWord:
                    return res
                
                for j in range(len(curWord)):
                    pattern = curWord[:j] + "*" + curWord[j + 1:]
                    for neiWord in graph[pattern]:
                        if neiWord not in visit:
                            visit.add(neiWord)
                            q.append(neiWord)
            res += 1
        return 0