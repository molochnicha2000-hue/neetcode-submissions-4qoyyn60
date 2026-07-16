# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1 = 0
        n2 = 0
        while l1:
            n1 = (n1 * 10) + l1.val
            l1 = l1.next
        
        while l2:
            n2 = (n2 * 10) + l2.val
            l2 = l2.next

        sn = str(n1 + n2)
        res = ListNode()
        i = 0
        dummy = ListNode(0, res)
        while i < len(sn):
            res.val = int(sn[i])
            i += 1
            if i < len(sn):
                res.next = ListNode()
                res = res.next

        return dummy.next