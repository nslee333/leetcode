import unittest
from typing import List


"""
Leetcode # 1342

Given an integer num, return the number of steps to reduce it to zero.

In one step, 
    if the current number is even, 
        you have to divide it by 2,
    otherwise, 
        you have to subtract 1 from it.

"""


class Solution:
    def fizz_buzz(self, num: int) -> List[str]:
        """
        Thoughts written out:
        
        We're trying to get to zero from n.
        
        Goal: we need to count how many steps it takes to get to zero.
        
        how can we reduce it to zero from n - we divide.
        
        if we divide by 2 there is a possibility that we will get a remainder.
        
        can we use modulo to sovle this?
        
        one case for odd one case for even
        
        every iteration we divide until we get to zero.
        
            - we might need to check if it is odd or even
                - if even:
                    divide by even number
                - if odd
                    divide by odd number?
            
        we count every iteration - then we return that number because it stands for how many steps it took to get to zero.
        
        
        """
        steps = 0
        
        while num > 0:
        
            if num % 2 == 0:
               num = num / 2
               steps += 1
               
            if num % 2 != 0:
                remainder = num % 2
                num = num - remainder 
                steps += 1
                
        return steps
                
        
        

class Test(unittest.TestCase):
    def test(self):
        s = Solution()
        
        input = 14
        expected = 6
        output = s.fizz_buzz(input)
        
        self.assertEqual(output, expected)
                
    def test2(self):
        s = Solution()
        
        input = 8
        expected = 4
        output = s.fizz_buzz(input)
        
        self.assertEqual(output, expected)
        
    def test3(self):
        s = Solution()
        
        input = 123
        expected = 12
        output = s.fizz_buzz(input)
        
        self.assertEqual(output, expected)

if __name__ == '__main__':
    unittest.main()