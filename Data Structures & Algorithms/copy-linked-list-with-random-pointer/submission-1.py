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
        cur = head
        memo = {None: None} # node : new_node

        while cur:
            copy = Node(cur.val)
            memo[cur] = copy      
            # new steps
            cur = cur.next
        
        cur = head
        
        while cur:
            copy = memo[cur]
            copy.next = memo[cur.next]
            copy.random = memo[cur.random]
            cur = cur.next

        return memo[head]
        

        