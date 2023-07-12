"""
Leetcode #5.

given a string s, return the longest palindromic substring in s.

"""

import unittest


class Solution(object):
    
    def longestPalindrome(self, s):
        return ""
    
    
    

class Test(unittest.TestCase):
    def test(self):
        s = Solution()
        
        input = "babad"
        expected = "bab"
        output = s.longestPalindrome(input)
        
        self.assertEqual(output, expected)
                
    def test2(self):
        s = Solution()
        
        input = "cbbd"
        expected = "bb"
        output = s.longestPalindrome(input)
        
        self.assertEqual(output, expected)

if __name__ == '__main__':
    unittest.main()