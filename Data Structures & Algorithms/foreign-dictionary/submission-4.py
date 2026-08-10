class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        N = len(words)
        adj = { c : set() for w in words for c in w}

        for i in range(N - 1):
            current = words[i]
            nxt = words[i + 1]
            L = min(len(current), len(nxt))

            if len(current) > len(nxt) and current[:L] == nxt[:L]:
                return ''

            for j in range(L):
                if current[j] != nxt[j]:
                    adj[current[j]].add(nxt[j])
                    break

        res = []
        visit = {}
        def dfs(node):
            if node in visit:
                return visit[node]

            visit[node] = True
            for nei in adj[node]:
                if dfs(nei):
                    return True
            visit[node] = False
            res.append(node)
        
        for char in adj:
            if dfs(char):
                return ''
        res.reverse()
        return ''.join(res)
        
