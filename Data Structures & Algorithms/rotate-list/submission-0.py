# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None

        storage = []
        current = head

        while current:
            storage.append(current.val)
            current = current.next

        N = len(storage)
        k %= N

        current = head
        for i in range(N - k, N):
            current.val = storage[i]
            current = current.next
        
        for i in range(N - k):
            current.val = storage[i]
            current = current.next
        return head