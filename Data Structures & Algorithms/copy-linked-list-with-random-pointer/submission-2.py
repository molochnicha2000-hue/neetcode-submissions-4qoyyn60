"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        current = head
        memo = {None : None}
        while current:
            c = Node(current.val)
            memo[current] = c
            current = current.next

        current = head
        while current:
            c = memo[current]
            c.next = memo[current.next]
            c.random = memo[current.random]
            current = current.next
        return memo[head]