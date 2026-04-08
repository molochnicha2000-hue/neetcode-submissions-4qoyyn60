class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = collections.defaultdict(list)

        for u, v, t in times:
            edges[u].append((v, t))

        minHeap = [(0, k)]
        res = 0
        visit = set()

        while minHeap:
            t1, n1 = heapq.heappop(minHeap)
            if n1 in visit:
                continue
            visit.add(n1)

            res = max(res, t1)
            for n2, t2 in edges[n1]:
                if n2 not in visit:
                    heapq.heappush(minHeap,(t2 + t1, n2))

        return res if len(visit) == n else -1

        