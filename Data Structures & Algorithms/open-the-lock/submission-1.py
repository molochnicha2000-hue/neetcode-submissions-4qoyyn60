class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1
        q = collections.deque([("0000", 0)])
        deadends = set(deadends)
        visit = set()
        while q:
            cur, steps = q.popleft()
            if cur == target:
                return steps
            
            if cur in deadends or cur in visit:
                continue
            visit.add(cur)
            for i in range(4):
                digit = int(cur[i])
                for step in [-1, 1]:
                    new = (digit + step) % 10
                    q.append((cur[:i] + str(new) + cur[i + 1:], steps + 1))
        return -1
                