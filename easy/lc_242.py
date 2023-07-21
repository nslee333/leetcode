import unittest


"""
Leetcode 242

Given two strings s and t, return true if t is an anagram of s and false otherwise.


"""



class Solution:
    def contains_duplicate(self, input, input_2):
        return False
            



class Test(unittest.TestCase):
    def test(self):
        s = Solution()
        
        input = "anagram"
        input_2 = "nagaram"
        expected = True
        output = s.contains_duplicate(input, input_2)
        
        self.assertEqual(output, expected)
                
    def test2(self):
        s = Solution()
        
        input = "rat"
        input_2 = "car"
        expected = False
        output = s.contains_duplicate(input, input_2)
        
        self.assertEqual(output, expected)
        

if __name__ == '__main__':
    unittest.main()



