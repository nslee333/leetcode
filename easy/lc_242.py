import unittest


"""
Leetcode 242

Given two strings s and t, return true if t is an anagram of s and false otherwise.


"""



class Solution:
    def contains_duplicate(self, input, input_2):
        # O(n + m) time complexity with a space complexity 0(n) to O(n + m)
        result = bool
        hash = {}

        arr_1 = [*input]
        arr_2 = [*input_2]
        
        if len(arr_1) != len(arr_2):
            return False
        
        for item in arr_1:
            if hash.get(item) == None:
                hash[item] = 0
            if hash.get(item) != None:
                hash[item] += 1
        
        for item in arr_2:
            if hash.get(item) == None:
                result = False
                break
            if hash.get(item) != None:
                hash[item] -= 1
        
        for value in hash.values():
            if value != 0:
                result = False
                break
            if value == 0:
                continue
            
        if result == bool:    
            result = True
        return result
    
    def contains_duplicate_2(self, s, t):
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
        
    def test3(self):
        s = Solution()
        
        input = "ab"
        input_2 = "a"
        expected = False
        output = s.contains_duplicate(input, input_2)
        
        self.assertEqual(output, expected)
        
    def test4(self):
        s = Solution()
        
        input = "anagram"
        input_2 = "nagaram"
        expected = True
        output = s.contains_duplicate_2(input, input_2)
        
        self.assertEqual(output, expected)
                
    def test5(self):
        s = Solution()
        
        input = "rat"
        input_2 = "car"
        expected = False
        output = s.contains_duplicate_2(input, input_2)
        
        self.assertEqual(output, expected)
        
    def test6(self):
        s = Solution()
        
        input = "ab"
        input_2 = "a"
        expected = False
        output = s.contains_duplicate_2(input, input_2)
        
        self.assertEqual(output, expected)
        

if __name__ == '__main__':
    unittest.main()



