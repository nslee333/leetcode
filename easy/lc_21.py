# python solution, convets to arrays, sorts and builds and returns result linked list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # taversal pointer for l1 and l2
        list_1 = convert(list1)
        list_2 = convert(list2)

        if len(list_1) == 0 and len(list_2) == 0:
            return None
        

        combo = list_1 + list_2
        combo.sort()

        res = ListNode()
        trav_res = res

        for i in range(len(combo)):
            trav_res.val = combo[i]
            
            if i == len(combo) - 1:
                break
            else:
                trav_res.next = ListNode()
                trav_res = trav_res.next
        return res

def convert(ll):
    res = []

    trav_ll = ll
    
    while trav_ll != None:
        res.append(trav_ll.val)
        trav_ll = trav_ll.next

    return res


# & Faster Python Solution

# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#     def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
#         l_1, l_2 = list1, list2

#         if not l_1 and not l_2:
#             return 
        
#         res = ListNode()
#         t_res = res

#         while True:
#             if not l_1 and not l_2:
#                 break
            
#             if not l_1:
#                 t_res.val = l_2.val
#                 l_2 = l_2.next

#             elif not l_2:
#                 t_res.val = l_1.val
#                 l_1 = l_1.next

#             if l_1 and l_2:
#                 if l_1.val <= l_2.val:
#                     t_res.val = l_1.val
#                     l_1 = l_1.next


#                 elif l_1.val > l_2.val:
#                     t_res.val = l_2.val
#                     l_2 = l_2.next

#             if l_1 or l_2:
#                 t_res.next = ListNode()
#                 t_res = t_res.next
#             else:
#                 t_res.next = None

#         return res
