# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# works, but too slow

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        # 1,2,3,4,5
        # 1,5,2,4,3

        trav = head
        arr = []

        while trav:
            arr.append(trav.val)
            trav = trav.next
        i, j = 0, len(arr) - 1

        reord = head
        while i <= j:
            
            # print(reord)                        
            reord.val = arr[i]
            i += 1
            if reord.next:
                reord = reord.next
                
                reord.val = arr[j]
                j -= 1
            reord = reord.next
        # print(head)
        # print(head)                                                 
