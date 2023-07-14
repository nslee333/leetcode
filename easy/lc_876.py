import unittest
from typing import Optional


"""
Given the head of a singly linked list, return the middle node of the linked list.

if there are two middle nodes, return the *second* middle node


"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
        
        
class Solution:
    def middle_node(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return ListNode(val=5, next = None)











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
            # if output.next != None and expected.next != None:
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