# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode(0, head)
        cur = head
        
        while cur.next:
            v1, v2 = cur.val, cur.next.val
            need = math.gcd(v1, v2)
            new = ListNode(need, cur.next)
            cur.next = new
            cur = cur.next.next
            
        return ans.next