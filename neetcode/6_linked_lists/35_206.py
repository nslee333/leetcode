# neetcode solution, O(n) time, O(1) space

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        
        while curr:
            nxt = curr.next
            curr.next = prev 
            prev = curr
            curr = nxt
        return prev



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# my solution, a bit slow.
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        current = head
        while current != None:
            stack.append(current.val)
            current = current.next

        if head == None:
            return None

        res_head = ListNode()
        stack.reverse()
        current_2 = res_head


        for i in range(len(stack)):
            print(stack[i])
            current_2.val = stack[i]
            new = ListNode()  

            if i < len(stack) - 1:

                current_2.next = new
                current_2 = current_2.next

        return res_head