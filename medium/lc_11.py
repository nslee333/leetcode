import unittest


"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

"""


class Solution:
    def single_number(self, nums):
       return 0



class Test(unittest.TestCase):
    def test(self):
        s = Solution()
        
        input = [1,8,6,2,5,4,8,3,7]
        expected = 49
        output = s.single_number(input)
        
        self.assertEqual(output, expected)
                
    def test2(self):
        s = Solution()
        
        input = [1,1]
        expected = 1
        output = s.single_number(input)
        
        self.assertEqual(output, expected)


if __name__ == '__main__':
    unittest.main()