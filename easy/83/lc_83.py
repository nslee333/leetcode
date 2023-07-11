# 
# Given the head of a sorted linked list
# Delete all duplicates such that each element
# appears only once.
# 
# Returned the linked list sorted as well.
# 


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def deleteDuplicates(head: ListNode) -> ListNode:
    current = head
                
    while current is not None and current.next is not None:
        if current.val == current.next.val:
            current.next = current.next.next
        else:
            current = current.next
    return head    