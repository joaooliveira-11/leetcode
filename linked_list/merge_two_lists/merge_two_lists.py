# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if not list1:
            return list2
        if not list2:
            return list1

        p1,p2 = list1, list2

        # Dummy node
        res = ListNode(-1)
        curr = res

        while p1 or p2:

            if not p1:
                curr.next = p2
                p2 = p2.next
                curr = curr.next
                continue
            if not p2:
                curr.next = p1
                p1 = p1.next
                curr = curr.next
                continue

            if p1.val < p2.val:
                curr.next = p1
                p1 = p1.next
                curr = curr.next
            else:
                curr.next = p2
                p2 = p2.next
                curr = curr.next
        
        return res.next



        
        