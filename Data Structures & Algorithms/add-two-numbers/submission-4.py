# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:       
        c1 = []
        while l1:
            c1.append(str(l1.val))
            l1 = l1.next

        c2 = []
        while l2:
            c2.append(str(l2.val))
            l2 = l2.next
        
        L = list(str(int(''.join(c2)[::-1]) + int(''.join(c1)[::-1])))
        #print(L)
        L = L[::-1]
        #print(L)
        res = ListNode()
        ans = res
        for i in range(len(L)):
            res.val = int(L[i])
            if i != len(L) - 1:
                res.next = ListNode()
                res = res.next
        return ans
