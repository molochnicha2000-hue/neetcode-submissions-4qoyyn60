# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        arr = []; cur = head
        while cur : 
            arr.append(cur.val)
            cur = cur.next
            
        new = []
        for i in range(len(arr) // 2 + 1):
            new.append(arr[i])
            if i != len(arr) - i - 1:
                new.append(arr[len(arr) - i - 1])

        i = 0
        cur = head
        while cur:
            cur.val = new[i]
            i += 1
            cur = cur.next
