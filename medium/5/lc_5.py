import unittest

"""
Leetcode #5.

given a string s, return the longest palindromic substring in s.

palindromic - forwards and backwards it reads the same

A palindrome is a minimum of 2 charactwers

"""

class Solution(object):
    
    def longestPalindrome(self, s):
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        start = 0
        maxLength = 1
        
        for i in range(n):
            dp[i][i] = True

        for i in range(n - 1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                start = i
                maxLength = 2

        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                    start = i
                    maxLength = length

        return s[start:start+maxLength]


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