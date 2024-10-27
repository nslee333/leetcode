import unittest


"""
Leetcode 242

Given two strings s and t, return true if t is an anagram of s and false otherwise.


"""

# faster solution, uses less memory
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        dict = {}

        for item in s:
            if item in dict:
                dict[item] += 1
            else:
                dict[item] = 1

        for item in t:
            if item not in dict:
                return False
            dict[item] -= 1
            if dict[item] < 0:
                return False
        
        for item in dict.values():
            if item > 0:
                return False
        return True






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
        if len(s) != len(t):
            return False
        
        s_arr, t_arr = [*s], [*t]
        hash_s, hash_t = {}, {}

        for s in s_arr:
            if hash_s.get(s) == None:
                hash_s[s] = 0
            if hash_s.get(s) != None:
                hash_s[s] += 1
                
        for t in t_arr:
            if hash_t.get(t) == None:
                hash_t[t] = 0
            if hash_t.get(t) != None:
                hash_t[t] += 1
        
        for key, value in hash_s.items():
            if hash_t.get(key) == None:
                return False
            if hash_t.get(key) == value:
                continue
            if hash_t.get(key) != value:
                return False
        return True


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
    def test7(self):
        s = Solution()
        
        input = "aacc"
        input_2 = "ccac"
        expected = False
        output = s.contains_duplicate_2(input, input_2)
        
        self.assertEqual(output, expected)
        

if __name__ == '__main__':
    unittest.main()



