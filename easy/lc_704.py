from typing import List


class Solution:
    def search(self, nums: List[int], target: int):
        start = 0
        mid = len(nums) // 2
        end = len(nums) - 1
        res = -1

        for i in range(len(nums)):
            if nums[mid] > target:
                end = mid - 1
                mid = (start + end) // 2
            elif nums[mid] < target:
                start = mid + 1
                mid = (start + end) // 2
            elif nums[mid] == target:
                res = mid
                break
        return res



import unittest

class Test(unittest.TestCase):
    def test(self):
        s = Solution()
        
        nums = [-1,0,3,5,9,12]
        target = 9
        expected = 4
        output = s.search(nums, target)
        
        self.assertEqual(output, expected)
                
    def test2(self):
        s = Solution()
        
        nums = [-1,0,3,5,9,12]
        target = 9
        expected = 4
        output = s.search(nums, target)
        
        self.assertEqual(output, expected)
        
    def test3(self):
        s = Solution()
        
        nums = [-1,0,5]
        target = 5
        expected = 2
        output = s.search(nums, target)
        
        self.assertEqual(output, expected)

if __name__ == '__main__':
    unittest.main()
