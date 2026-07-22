# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        memo = []
        current = head

        while current:
            memo.append(current)
            current = current.next
        
        N = len(memo)
        timer = 0
        for i in range(N // 2):
            tmp = memo[i].next
            nxt = memo[N - i - 1]

            memo[i].next = nxt
            nxt.next = tmp
        memo[N // 2].next = None