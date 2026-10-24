# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge(L1, L2):
            ans = ListNode()
            A = ans
            c1, c2 = L1, L2
            while c1 and c2:
                if c1 and c2:
                    if c1.val < c2.val:
                        nxt = ListNode(c1.val)
                        c1 = c1.next
                    else:
                        nxt = ListNode(c2.val)
                        c2 = c2.next
                ans.next = nxt
                ans = ans.next
            if c1:
                ans.next = c1
            elif c2:
                ans.next = c2
            return A.next

        def dfs(l, r):
            if l > r : return None
            if l == r : return lists[l]
            m = (l + r) // 2
            left = dfs(l, m)
            right = dfs(m + 1, r)
            return merge(left, right)
        return dfs(0, len(lists) - 1)