import unittest
from typing import List


"""
Leetcode # 383

Given two strings randsomNote and magazine, 
    if randomNote can be constructed using the letters from magazine
        return True
    else
        return false
        
Each letter can only be used once in randomNote

"""




class Solution:
   def canConstruct(self, ransomNote: str, magazine: str) -> bool:
       return False
        


class Test(unittest.TestCase):
    def test(self):
        s = Solution()
        
        input_a = "a"
        input_b = "b"
        expected = False
        output = s.canConstruct(input_a, input_b)
        
        self.assertEqual(output, expected)
                
    def test2(self):
        s = Solution()
        
        input_a = "aa"
        input_b = "ab"
        expected = False
        output = s.canConstruct(input_a, input_b)
        
        self.assertEqual(output, expected)
        
    def test3(self):
        s = Solution()
        
        input_a = "aa"
        input_b = "aab"
        expected = True
        output = s.canConstruct(input_a, input_b)
        
        self.assertEqual(output, expected)

if __name__ == '__main__':
    unittest.main()