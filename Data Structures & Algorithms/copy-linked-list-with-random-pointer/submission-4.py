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
        cache = {None : None}
       
        while current:
            copy = Node(current.val)
            cache[current] = copy

            current = current.next
     
        current = head
        while current:
            f1 = cache[current]

            f1.random = cache[current.random]
            f1.next = cache[current.next]

            current = current.next
        return cache[head]