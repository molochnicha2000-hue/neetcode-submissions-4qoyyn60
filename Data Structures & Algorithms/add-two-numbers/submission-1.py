# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        list_of_all = []
        cur = l1
        temp = []
        while cur:
            temp.append(str(cur.val))
            cur = cur.next
        list_of_all.append(temp)

        cur = l2
        temp = []
        while cur:
            temp.append(str(cur.val))
            cur = cur.next
        list_of_all.append(temp)

        num1, num2 = list_of_all
        num1 = "".join(num1)[::-1]
        num2 = "".join(num2)[::-1]
        
        N = max(len(num1), len(num2))
        if len(num1) > len(num2):
            num1 += "0" * (N - len(num1))
        elif len(num1) < len(num2):
            num2 += "0" * (N - len(num2))
        
        res = str(int(num1) + int(num2))
        print(res)
        i = len(res) - 1 
        cur = ListNode(int(res[i]))
        res_link = cur
        while i != 0:
            i -= 1
            cur.next = ListNode(int(res[i]))
            cur = cur.next
        return res_link