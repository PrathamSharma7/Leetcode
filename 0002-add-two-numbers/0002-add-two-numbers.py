# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1 = ""
        n2 = ""

        while l1 is not None:
            n1 += str(l1.val)
            l1 = l1.next

        while l2 is not None:
            n2 += str(l2.val)
            l2 = l2.next

        n1 = int(n1[::-1])
        n2 = int(n2[::-1])

        total = n1 + n2
        total = str(total)[::-1]

        dummy = ListNode()
        curr = dummy

        for digit in total:
            curr.next = ListNode(int(digit))
            curr = curr.next

        return dummy.next