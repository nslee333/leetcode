"""
    You are given two non-empty linked lists representing two non-negative integers. 

    The digits are stored in reverse order and each of their nodes contains a single digit. 

    Add the two numbers and return the sum as a linked list.

    You may assume the two numbers do not contain any leading zero, execept the number 0 itself.


"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def convertLLtoArr(l1: ListNode):
    current = l1
    arr = []
    
    while current != None:
        arr.append(current.val)
        current = current.next
    return arr


def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    dummy = ListNode(0)
    current = dummy
    carry = 0
    
    while l1 or l2 or carry:
        x = l1.val if l1 else 0
        y = l2.val if l2 else 0

        sum_val = carry + x + y
        carry = sum_val // 10
        digit = sum_val % 10
        
        current.next = ListNode(digit)
        current = current.next
        
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next
    
    if carry > 0:
        current.next = ListNode(carry)
        
    return dummy.next



