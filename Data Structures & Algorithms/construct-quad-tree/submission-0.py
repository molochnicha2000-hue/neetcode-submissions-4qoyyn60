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
        N = len(grid) # N == R == C
        # self.isLeaf == True if and only if M * M values equal  
        def dfs(N, r, c):
            check = True
            for i in range(N):
                for j in range(N):
                    if grid[r][c] != grid[r + i][c + j]:
                        check = False
                        break
            N //= 2
            if not check:
                # can go into recursion
                topLeft = dfs(N, r, c)
                topRight = dfs(N, r, c + N)
                bottomLeft = dfs(N, r + N, c)
                bottomRight = dfs(N, r + N, c + N)
                return Node(0, False, topLeft, topRight, bottomLeft, bottomRight)
            else:
                return Node(grid[r][c], True)

        return dfs(N, 0, 0)
            





















