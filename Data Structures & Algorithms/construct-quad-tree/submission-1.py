"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        N = len(grid)

        def dfs(N, r, c):
            check = True
            for i in range(N):
                for j in range(N):
                    if grid[r + i][c + j] != grid[r][c]:
                        check = False
                        break
            N //= 2
            if not check:
                topleft = dfs(N, r, c)
                topright = dfs(N, r, c + N)
                bottomleft = dfs(N, r + N, c)
                bottomright = dfs(N, r + N, c + N)

                return Node(0, False, topleft, topright, bottomleft, bottomright)
            else:
                return Node(grid[r][c], True)
        return dfs(N, 0, 0)