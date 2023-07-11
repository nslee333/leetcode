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
    l1current = l1
    l2current = l2
    
    
    current = []
    while l1current != None and l2current != None:
        # print(l1current.next)
        # print(l2current.next)
        if l1current.val + l2current.val < 10:
            current.append(l1current.val + l2current.val)
            
            l1current = l1current.next
            l2current = l2current.next
            
        else:
            num = l1current.val + l2current.val
            nums = [int(x) for x in str(num)]
            current.append(nums[-1])
            
            if l1current.next != None:
                l1current.next.val += nums[0]
            else:
                current.append(nums[0])
            # print(current)
            
            l1current = l1current.next
            l2current = l2current.next
    
    head = ListNode(val = 0, next = None)
    head_current = head
    
    for i in range(len(current)):
        
        head_current.val = current[i]
        
        if i < len(current)-1 and current[i+1] != None:
            head_current.next = ListNode(val = 0, next = None)
        else:
            head_current.next = None
        head_current = head_current.next


    
    # x = head
    # print("start here")
    # print(current)
    # while x != None:
    #     print(x.val)
    #     print(x.next)
    #     x = x.next
            
            
            
    return head
    


