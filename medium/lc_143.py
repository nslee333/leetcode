# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# apparently this does work? leetcode is weird

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        trav = head
        arr = []

        while trav:
            arr.append(trav.val)
            trav = trav.next
        i, j = 0, len(arr) - 1

        reord = head
        while i <= j:
            
            reord.val = arr[i]
            i += 1
            if reord.next:
                reord = reord.next
                
                reord.val = arr[j]
                j -= 1
            reord = reord.next
