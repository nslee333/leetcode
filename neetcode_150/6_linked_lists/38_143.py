# reorder list, this code isn't working, and don't know if it's a good idea yet

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.next = next

    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head

        temp = None
        while fast and fast.next:
            temp = fast
            fast = fast.next

            temp = fast
            fast = fast.next

            slow = slow.next
        
        # reverse the 2nd list

        temp = None
        prev = None

        while slow:
            temp = slow
            slow = slow.next