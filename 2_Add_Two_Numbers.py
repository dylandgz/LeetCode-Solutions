
// Your code here
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p1 = l1
        p2 = l2
        v1 = 0
        v2 = 0
        carryover = 0
        tempHead = ListNode()
        p 3 =tempHead
        while p1 or p2:
            if p1:
                v1 = p1.val
            else: v1 = 0

            if p2:
                v2 = p2.val
            else:
                v2 = 0

            res = v1 + v2 + carryover

            if res > 9:
                res -= 10
                carryover = 1
            else:
                carryove r =0



            p3.nex t =ListNode(res)
            p 3 =p3.next
            if p1 and p2:
                p 1 =p1.next
                p 2 =p2.next
            elif p1:
                p 1 =p1.next
            else:
                p 2 =p2.next
        if carryover == 1:
            p3.next = ListNode(carryover)
        return tempHead.next
