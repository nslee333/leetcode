import unittest
from typing import Optional


"""
Leetcode # 876

Given the head of a singly linked list, return the middle node of the linked list.

if there are two middle nodes, return the *second* middle node


"""
"""
Thought process:

we need to find the middle node of a linked list -

What do we need?

We need to find the length of the linked list
    - How do we find it?
    
    - We can go through and count how many vals there are.
        - Keep a running count of the vals. 
            - Route #1
        - push the vals into an array then return the length of the array.
            - Route #2
        
Once we have the length - we then need to divide by 2. 
    Let's try it with an array.

if the length of the array is odd - we can just return the middle element.
if the length of the array is even - we can return the 2nd middle element.

Now we know what element we're going for we write another loop:

loop through the lined list
    if ListNode.val == target:
        return the current ListNode.
        
return ListNode.

"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def middle_node(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        current = head
        vals = []
        
        while current != None:
            vals.append(current.val)
            current = current.next
            
        if len(vals) % 2 != 0:
            middle_index = len(vals) // 2
            
            
        elif len(vals) %2 == 0:
            middle_index = len(vals) / 2
        
        current = head
        
        while current != None:
            if middle_index == 0:
                break
            else:
                middle_index -= 1
                current = current.next
                
        return current
    

class Test(unittest.TestCase):
    def test(self):
        s = Solution()
        
        input = ListNode(val = 1, next = 
                         ListNode(val = 2, next = 
                                  ListNode(val = 3, next = 
                                           ListNode(val = 4, next = 
                                                    ListNode(val = 5, next = None)))))
        
        
        expected = ListNode(val = 3, next = 
                         ListNode(val = 4, next = 
                                  ListNode(val = 5, next = None)))
        
        output = s.middle_node(input)
        
        while output != None:
            self.assertEqual(output.val, expected.val)
            expected = expected.next
            output = output.next
        
                
    def test2(self):
        s = Solution()
        
        input = ListNode(val = 1, next = 
                         ListNode(val = 2, next = 
                                  ListNode(val = 3, next = 
                                           ListNode(val = 4, next = 
                                                    ListNode(val = 5, next = 
                                                             ListNode(val = 6, next = None))))))
        
        
        expected = ListNode(val = 4, next = 
                         ListNode(val = 5, next = 
                                  ListNode(val = 6, next = None)))
        
        output = s.middle_node(input)
        
        while output != None:
            self.assertEqual(output.val, expected.val)
            expected = expected.next
            output = output.next

if __name__ == '__main__':
    unittest.main()