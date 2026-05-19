# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        storage = []
        cur = head
        while cur:
            storage.append(cur)
            cur = cur.next
        
        i, j = 0, len(storage) - 1
        while i < j:
            storage[i].next = storage[j]
            i += 1
            if i >= j:
                break
            storage[j].next = storage[i]
            j -= 1
        storage[j].next = None