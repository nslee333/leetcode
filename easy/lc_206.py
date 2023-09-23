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
        for i in range(len(temp) - 1, -1, -1):
            rev_current.val = temp[i]
            if i == 0:
                rev_current.next = None
            else:
                rev_current.next = ListNode()
                rev_current = rev_current.next
            print(reversed_list)

        return reversed_list