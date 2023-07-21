import unittest


"""
# 136. Single Number

Given a non-empty array of integers nums, every element appears twice execpt for one.

Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space


"""


class Solution:
    def single_number(self, nums):
        result = 0
        hash = {}
        
        for i in range(len(nums)):
            if hash.get(nums[i]) == None:
                hash[nums[i]] = 0
                
            if hash.get(nums[i]) != None:
                hash[nums[i]] += 1
            
        for key, value in hash.items():
            if value == 1:
                result = key
                  
        
        return result
        
# Try to use the XOR (^) operation, 
# which can help you find the unique element in the array without using extra space.

        return result









class Test(unittest.TestCase):
    def test(self):
        s = Solution()
        
        input = [2,2,1]
        expected = 1
        output = s.single_number(input)
        
        self.assertEqual(output, expected)
                
    def test2(self):
        s = Solution()
        
        input = [4,1,2,1,2]
        expected = 4
        output = s.single_number(input)
        
        self.assertEqual(output, expected)

    def test3(self):
        s = Solution()
        
        input = [1]
        expected = 1
        output = s.single_number(input)
        
        self.assertEqual(output, expected)

if __name__ == '__main__':
    unittest.main()