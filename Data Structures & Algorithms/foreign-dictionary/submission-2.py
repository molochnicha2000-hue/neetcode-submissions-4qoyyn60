class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adg = {c:set() for w in words for c in w}

        for c in range(len(words) - 1):
            w1, w2 = words[c], words[c + 1]
            minLen = min(len(w1), len(w2))

            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""

            for j in range(minLen):
                if w1[j] != w2[j]:
                    adg[w1[j]].add(w2[j])
                    break
        res = []
        visit = {}
        def dfs(c):
            if c in visit:
                return visit[c]
        
            visit[c] = True
            for nei in adg[c]:
                if dfs(nei): return True

            visit[c] = False
            res.append(c)
            return False

        for c in adg:
            if dfs(c): 
                return ""

        res.reverse()
        return "".join(res)
            
        

        