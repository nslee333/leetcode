import unittest


"""
Leetcode 217

Given an integer array nums, return true if any value appears at least twice in the array, 
and return false if every element is distinct.


"""



class Solution:
    def contains_duplicate(self, nums):
        result = bool
                
        nums.sort()
            
        for i in range(len(nums)):
            if i < len(nums)-1:
                if nums[i] == nums[i+1]:
                    result = True
            
        if result == bool:
            result = False
                    
        return result
    
    
    def contains_duplicate_hashset(self, nums):
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False
            



class Test(unittest.TestCase):
    def test(self):
        s = Solution()
        
        input = [1,2,3,1]
        expected = True
        output = s.contains_duplicate(input)
        
        self.assertEqual(output, expected)
                
    def test2(self):
        s = Solution()
        
        input = [1,2,3,4]
        expected = False
        output = s.contains_duplicate(input)
        
        self.assertEqual(output, expected)
        
    def test3(self):
        s = Solution()
        
        input = [1,1,1,3,3,4,3,2,4,2]
        expected = True
        output = s.contains_duplicate(input)
        
        self.assertEqual(output, expected)
        
    def test4(self):
        s = Solution()
        
        input = [1,2,3,1]
        expected = True
        output = s.contains_duplicate_hashset(input)
        
        self.assertEqual(output, expected)
                
    def test5(self):
        s = Solution()
        
        input = [1,2,3,4]
        expected = False
        output = s.contains_duplicate_hashset(input)
        
        self.assertEqual(output, expected)
        
    def test6(self):
        s = Solution()
        
        input = [1,1,1,3,3,4,3,2,4,2]
        expected = True
        output = s.contains_duplicate_hashset(input)
        
        self.assertEqual(output, expected)

if __name__ == '__main__':
    unittest.main()



