class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = {i : [] for i in range(len(edges) + 1)}
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        res = set()
        visit = set()

        def dfs(cur, parent):         
            if cur in visit:
                return False
            
            visit.add(cur)
            for i in graph[cur]:
                if i == parent:
                    continue
                if  not dfs(i, cur):
                    edge = (min(cur, i), max(cur, i))
                    res.add(edge)
            
            visit.remove(cur)
            return True

        for i, neigh in graph.items():
            for j in neigh:
                dfs(j, i)
        
        N = len(edges)
        for i in range(N - 1, -1, -1):
            edge_tuple = (min(edges[i]), max(edges[i]))
            if edge_tuple in res:
                return edges[i]
        
        return []