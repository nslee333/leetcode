import unittest
from typing import List


"""
Leetcode # 1342

Given an integer num, return the number of steps to reduce it to zero.

In one step, if the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.

"""




class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
       return 0
   

class Test(unittest.TestCase):
    def test(self):
        s = Solution()
        
        input = 14
        expected = 6
        output = s.fizzBuzz(input)
        
        self.assertEqual(output, expected)
                
    def test2(self):
        s = Solution()
        
        input = 8
        expected = 4
        output = s.fizzBuzz(input)
        
        self.assertEqual(output, expected)
        
    def test3(self):
        s = Solution()
        
        input = 123
        expected = 12
        output = s.fizzBuzz(input)
        
        self.assertEqual(output, expected)

if __name__ == '__main__':
    unittest.main()