class CountSquares:
    def __init__(self):
        self.storage = []
        self.Count = collections.defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.storage.append(point)
        self.Count[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        ans = 0
        px, py = point
        for x, y in self.storage:
            if (abs(x - px) != abs(y - py)) or x == px or y == py:
                continue
            ans += self.Count[(x, py)] * self.Count[(px, y)]
        return ans