import unittest
from collections import defaultdict

"""
Leetcode 271 encode and decode strings

"""

class Solution:
    # Neetcode example
    def encode(self, strs):
        result = ""
        for item in strs:
            result += str(len(item)) + "#" + item
        return result
    
    def decode(self, str):
        res, i = [], 0
        
        while i < len(str):
            j = i
            while str[j] != "#":
                j += 1
            length = int(str[i:j])
            res.append(str[j + 1 : j + 1 + length])
            i = j + 1 + length
        return res
    
    # My code - decode is broken
    
    # def encode(self, strs):
    #     res = ""
    #     for s in strs:
    #         res += str(len(s)) + "#" + s
    #     return res
    
    
    
    
    # def decode(self, str):
    #     str = [*str]
    #     result = []
    #     i = 0
    #     while i < len(str)-1:
    #         word = ""
    #         if type(str[i]) == int and str[i+1] == "#": # problem is here
    #             for item in range(str[i]):
    #                 word += item
    #             result.append(word)
    #             chars = str[i]
    #             i += 2 + chars
            
    #         else:
    #             i += 1
    #     print(result)
    #     return result

class Test(unittest.TestCase):
    def test(self):
        s = Solution()
        
        
        # Test case 1: Basic case with two strings
        input_strings = ["hello", "world"]
        encoded = s.encode(input_strings)
        decoded = s.decode(encoded)
        self.assertEqual(decoded, input_strings)
    def test2(self):
        s = Solution()
        # Test case 2: Empty string
        input_strings = [""]
        encoded = s.encode(input_strings)
        decoded = s.decode(encoded)
        self.assertEqual(decoded, input_strings)
    def test3(self):
        s = Solution()
        # Test case 3: Strings with special characters
        input_strings = ["a#", "#b", "c#d#e"]
        encoded = s.encode(input_strings)
        decoded = s.decode(encoded)
        self.assertEqual(decoded, input_strings)
        
    def test4(self):
        s = Solution()
        # Test case 4: Multiple strings
        input_strings = ["apple", "banana", "cherry", "date"]
        encoded = s.encode(input_strings)
        decoded = s.decode(encoded)
        self.assertEqual(decoded, input_strings)

if __name__ == '__main__':
    unittest.main()