import unittest


"""
Leetcode 49

Given an array of strings, group the anagrams together. You can return the answer in any order.

"""


class Solution:
    def group_anagrams(self, nums):
       return 0



class Test(unittest.TestCase):
    def test(self):
        s = Solution()
        
        input = ["eat","tea","tan","ate","nat","bat"]
        expected = [["bat"],["nat","tan"],["ate","eat","tea"]]
        output = s.group_anagrams(input)
        
        self.assertEqual(output, expected)
                
    def test2(self):
        s = Solution()
        
        input = [""]
        expected = [[""]]
        output = s.group_anagrams(input)
        
        self.assertEqual(output, expected)

    def test2(self):
        s = Solution()
        
        input = ["a"]
        expected = ["a"]
        output = s.group_anagrams(input)
        
        self.assertEqual(output, expected)


if __name__ == '__main__':
    unittest.main()