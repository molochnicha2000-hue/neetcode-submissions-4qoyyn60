# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        n = len(lists)     
        def merge(A, B):
            ans = ListNode()
            a = ans
            A1, B1 = A, B
            while A1 and B1:
                if A1.val > B1.val:
                    ans.next = ListNode(B1.val)
                    B1 = B1.next
                else:
                    ans.next = ListNode(A1.val)
                    A1 = A1.next
                ans = ans.next
            if A1:
                ans.next = A1
            elif B1:
                ans.next = B1
            return a.next


        def dfs(l, r):
            if l > r : return None
            if l == r : return lists[l]
            m = (l + r) // 2
            left = dfs(l, m)
            right = dfs(m + 1, r)
            return merge(left, right)
        return dfs(0, n - 1)

