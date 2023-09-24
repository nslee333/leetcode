# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
            
        temp = []
        current = head
        reversed_list = ListNode()
        while current != None:
            temp.append(current.val)
            current = current.next
        
        rev_current = reversed_list
        while rev_current != None:
            
            rev_current.val = temp.pop()
            if len(temp) == 0:
                rev_current.next = None
                break
            else:
                rev_current.next = ListNode()
                rev_current = rev_current.next

        return reversed_list