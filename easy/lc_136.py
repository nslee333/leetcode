import unittest


"""
# 136. Single Number

Given a non-empty array of integers nums, every element appears twice execpt for one.

Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space


"""




class Solution:
    def single_number(self, nums):
        # print(nums)
        result = 0
        hash = {}
        
        # print(len(nums))
        for i in range(len(nums)):
            # print(i)
            # print(nums[i], "HIH")
            if hash.get(i) == None:
                hash[i] = 1 # key index to value int
            if hash.get(i) == nums[i]:
                hash[i] += 1
                print(i, "i")
                print(hash[i], "hash[i]")
            
        for j in range(len(nums)):
            # print(j)
            if hash.get(j) == nums[j]:
                hash[j] -= 1
                print(hash[j], "hash[j]")
                print(j, "j")
            
        for h in hash:
            if h == 1:
                # print(nums[h], "result")
                # print(h, "h")
                result = nums[h]
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