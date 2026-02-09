# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head or not head.next:
            return

        list_len = 0
        curr = head

        while curr:
            list_len +=1
            curr = curr.next

        pos_to_remove = list_len - n
        counter = 0

        prev = None
        curr = head
        while True:
            temp_next = curr.next
            if counter == pos_to_remove:
                if prev is not None:
                    prev.next = temp_next
                curr.next = None
                return head if counter != 0 else temp_next
            
            prev = curr
            curr = curr.next
            counter+=1
            
                