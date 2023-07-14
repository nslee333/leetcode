import unittest

"""
Leetcode 1480

Given an array nums. We define a running sum of an array as runnungSum[i] = sum(nums[0]...nums[i])

return the running sum of nums

"""

class Solution:
    # Results array approach
    def runningSum(self, nums):
        count = []
        count.append(nums[0])

        for i in range(len(nums)):
            if i < len(nums)-1:
                count.append(count[i] + nums[i+1])

        return count
    
    # overwritten input approach
    def runningSum2(self, nums):
        i = 1
        while i < len(nums):
            nums[i] = nums[i] + nums[i-1]
            i += 1

        return nums  



class Test(unittest.TestCase):
    def test(self):
        s = Solution()
        
        input = [1,2,3,4]
        expected = [1,3,6,10]
        output = s.runningSum(input)
        
        self.assertEqual(output, expected)
                
    def test2(self):
        s = Solution()
        
        input = [1,1,1,1,1]
        expected = [1,2,3,4,5]
        output = s.runningSum(input)
        
        self.assertEqual(output, expected)
        
    def test3(self):
        s = Solution()
        
        input = [3,1,2,10,1]
        expected = [3,4,6,16,17]
        output = s.runningSum(input)
        
        self.assertEqual(output, expected)

if __name__ == '__main__':
    unittest.main()