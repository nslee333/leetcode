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
"""
Thought Process:

1. We need to check if the letters from magazine are in random note.
2. each letter in magizine can only be used once.

We need to return true or false if we can contruct the random note from the magazine.

We can't use a list because magazine can have duplicate characters.

We might be able to use a hash table for quick lookup.

pesudocode:

convert magazine into an array.

init a hash table

loop over magazine array
    we push index i as the key and arr[index] as the value to the hash table
    ^ I don't think above will necessarily work - 

convert random note into array

loop over the randsomNote array
    if i 
    
My though process got lost as I ran into a road block with not knowing what I can do with hash maps
"""


class Solution:
   def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        # This solution has an O(n + m) time complexity -> n = magazine's length and m = note's length
        # This solution has an O(n + m) space complexity -> because we created:
        # mag -> list of magazine, note -> list of note, and hash which is a dictionary 
        
        
        mag = list(magazine)
        note = list(ransomNote)
        
        if len(note) > len(mag):
            return False
        
        hash = {}
                
        for letter in mag:
            if letter not in hash:
                hash[letter] = 1
            else:
                hash[letter] += 1
    
        for letter in note:
            if letter not in hash:
                return False
            elif hash.get(letter) >= 1:
                hash[letter] -= 1
            else:
                return False
        return True            
        


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