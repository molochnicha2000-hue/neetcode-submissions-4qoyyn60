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
        cache = {None : None}
        current = head
        while current:
            copy = Node(current.val)
            cache[current] = copy
            current = current.next

        
        current = head
        while current:
            c = cache[current]
            c.next = cache[current.next]
            c.random = cache[current.random]
            current = current.next

        return cache[head]