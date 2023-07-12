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
        
        for i, e in [("babad", "bab")]:
            
            if self.assertEqual(s.longestPalindrome(i), e) == False:
                print(i,e)
                
    def test2(self):
        s = Solution()
        
        for i, e in [("string", "string")]:
            
            if self.assertEqual(s.longestPalindrome(i), e) == False:
                print(i,e)

    def test3(self):
        s = Solution()
        
        for i, e in [("string", "string")]:
            
            if self.assertEqual(s.longestPalindrome(i), e) == False:
                print(i,e)
    
if __name__ == '__main__':
    unittest.main()