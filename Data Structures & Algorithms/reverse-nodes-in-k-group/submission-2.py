# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        current = head
        storage = []
        while current:
            storage.append(current.val)
            current = current.next
        
        res = []
        N = len(storage)
        i = 0
        while i < N:
            temp = []
            prev = i
            while prev < N and prev - i < k:
                temp.append(storage[prev])
                prev += 1

            if len(temp) == k:
                for x in reversed(temp):
                    res.append(x)
            else:
                for x in temp:
                    res.append(x)
            i = prev
        
        ans = ListNode()
        r = ans
        for x in res:
            nxt = ListNode(x)
            ans.next = nxt
            ans = ans.next
        return r.next