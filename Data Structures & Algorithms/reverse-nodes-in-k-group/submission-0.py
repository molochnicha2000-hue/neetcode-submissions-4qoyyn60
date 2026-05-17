# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        storage = []
        cur = head
        while cur:
            storage.append(cur.val)
            cur = cur.next
        
        i = 0
        new_storage = []
        while i < len(storage) and len(storage[i : i + k]) % k == 0:
            new_storage.append(storage[i : i + k][::-1])
            i += k
        
        if len(storage) - i != 0:
            new_storage.append(storage[i:])
        
        final_storage = []
        for i in new_storage:
            for j in i:
                final_storage.append(j)
        
        N = len(final_storage)
        i = 0

        res = ListNode(final_storage[0])
        cur = res
        for val in final_storage[1:]:
            cur.next = ListNode(val)
            cur = cur.next


        return res