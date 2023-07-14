import unittest

"""
Leetcode #2235

return the sum of two numbers

"""


class Solution:
    def sum(self, num1, num2):
        return num1 + num2


class Test(unittest.TestCase):
    def test(self):
        s = Solution()
        
        input1 = 1
        input2 = 1
        expected = 2
        output = s.sum(input1, input2)
        
        self.assertEqual(output, expected)
                
    def test2(self):
        s = Solution()
        
        input1 = 3
        input2 = 4
        expected = 7
        output = s.sum(input1, input2)
        
        self.assertEqual(output, expected)

if __name__ == '__main__':
    unittest.main()
