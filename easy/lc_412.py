import unittest
from typing import List


"""
Leetcode # 412
Given an integer n, return a string array answer (1-indexed) where:

answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i (as a string) if none of the above conditions are true.

"""




class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = []
        
        for i in range(1, n + 1):
            if i < 3:
                result.append(f"{i}")
        
            elif i % 3 == 0 and i % 5 == 0:
                result.append("FizzBuzz")
                
            elif i % 3 == 0:
                result.append("Fizz")
                
            elif i % 5 == 0:
                result.append("Buzz")
            else:
                result.append(f"{i}")
                
        return result


class Test(unittest.TestCase):
    def test(self):
        s = Solution()
        
        input = 3
        expected = ["1","2","Fizz"]
        output = s.fizzBuzz(input)
        
        self.assertEqual(output, expected)
                
    def test2(self):
        s = Solution()
        
        input = 5
        expected = ["1","2","Fizz","4","Buzz"]
        output = s.fizzBuzz(input)
        
        self.assertEqual(output, expected)
        
    def test3(self):
        s = Solution()
        
        input = 15
        expected = ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]
        output = s.fizzBuzz(input)
        
        self.assertEqual(output, expected)

if __name__ == '__main__':
    unittest.main()