# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # The goal here is to take advantage 
        # of fast and slow pointer approach

        if not head or not head.next:
            return

        slow_p, fast_p = head, head.next

        # find the middle of the list
        while fast_p and fast_p.next:       
            slow_p, fast_p = slow_p.next, fast_p.next.next

        # pointer to the second half
        second_l = slow_p.next
        slow_p.next = None

        # reverse the second half
        curr = second_l

        prev = None
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        # merge both halfs
        first = head
        second = prev

        while second:
            next_p1 = first.next
            next_p2 = second.next

            first.next = second
            second.next = next_p1

            first = next_p1
            second = next_p2
    


        
        




            
        

        

        