# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next 

# this is my solution :)
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
      if head == None: return None
      current = head
      li = []

      while current != None:
        li.append(current.val)
        current = current.next
      li.reverse()

      rev = ListNode()
      rev_cur = rev
      for i in range(len(li)):
        rev_cur.val = li[i]
        if i == len(li) - 1:
          rev_cur.next = None
        else:
          rev_cur.next = ListNode()
        rev_cur = rev_cur.next
      return rev
