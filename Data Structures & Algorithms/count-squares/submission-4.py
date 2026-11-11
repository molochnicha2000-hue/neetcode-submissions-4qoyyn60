class CountSquares:
    def __init__(self):
        self.storage = []
        self.f = collections.Counter() 

    def add(self, point: List[int]) -> None:
        self.storage.append(point)
        self.f[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        res = 0
        x1, y1 = point
        skip = set()
        for x2, y2 in self.storage:
            if (x2, y2) in skip:
                continue
            if abs(x2 - x1) != abs(y2 - y1) or x2 == x1 or y1 == y2:
                continue

            x3, y3 = x2, y1
            x4, y4 = x1, y2
            if ((x3, y3) in self.f and (x4, y4) in self.f and 
                abs(x3  - x4) == abs(y4 - y3)):
                """
                current = max(self.f[(x4, y4)],
                            self.f[(x3, y3)], 
                            self.f[(x2, y2)], 
                            self.f[(x1, y1)] + 1)
                """
                """
                skip.add((x4, y4))
                skip.add((x3, y3))
                skip.add((x2, y2))
                """
                res += max(self.f[(x3, y3)] * self.f[(x4, y4)], 
                        self.f[(x1, y1)] * self.f[(x2, y2)])
        return res
