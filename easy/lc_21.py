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

# & Go Solution, not my own.

# func mergeTwoLists(l1 *ListNode, l2 *ListNode) *ListNode {
# 	dummy := &ListNode{}

# 	current := dummy

# 	for l1 != nil && l2 != nil {
# 		if l1.Val <= l2.Val {
# 			current.Next = l1
# 			l1 = l1.Next
# 		} else {
# 			current.Next = l2
# 			l2 = l2.Next
# 		}
# 		current = current.Next

# 	}

# 	if l1 != nil {
# 		current.Next = l1
# 	} else {
# 		current.Next = l2
# 	}

# 	return dummy.Next
# }



