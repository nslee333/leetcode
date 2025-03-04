# reorder list, this code isn't working, and don't know if it's a good idea yet

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        res = head

        count = 0

        current = head
        while current:
            count += 1
            current = current.next
        
        n_elements = math.ceil(count // 2)

        count = 0
        current = head
        array = []

        while current:
            if count >= n_elements:
                array.insert(0, current.val)

            count += 1
            current = current.next
        print(array)

        count = 0
        temp = 0
        current = res
        while current:
            if count % 2 == 0:
                temp = current.val
                current.val = array.pop(0)
            elif count % 2 > 0 and count is not 0:
                current.val = temp
                
            count += 1
            current = current.next
        return res
        