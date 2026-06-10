# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        res = []
        cur = head
        index1, index2 = None, None
        while cur:
            res.append(cur.val)
            cur = cur.next
            
        res = res[:left - 1] + res[left - 1: right][::-1] + res[right: ] 
        ans = ListNode()
        cur = ans
        i = 0 
        while i < len(res):
            cur.next = ListNode(res[i])
            cur = cur.next
            i += 1

        return ans.next