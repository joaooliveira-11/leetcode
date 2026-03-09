# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        aux = []

        curr = head

        while curr:
            aux.append(curr)
            curr = curr.next

        to_remove_idx = len(aux) - n
        if to_remove_idx == 0:
            res = aux[to_remove_idx].next
            aux[to_remove_idx].next = None
            return res

        to_remove = aux[to_remove_idx]
        prev_t_remove = aux[len(aux) - n -1]

        prev_t_remove.next = to_remove.next
        to_remove.next = None

        return head





        