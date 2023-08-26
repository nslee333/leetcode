import unittest


"""
Leetcode 11

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

"""
class Solution:
    def maxArea(self, height):
        largest_area = 0
        i = 0
        j = len(height) - 1

        while i < j:
            print(largest_area)
            if height[i] < height[j]:
                if height[i] * (j - i) > largest_area:
                    largest_area = height[i] * (j - i)
                i += 1
            elif height[i] > height[j]:
                if height[j] * (j - i) > largest_area:
                    largest_area = height[j] * (j - i)
                j -= 1
            elif height[i] == height[j]:
                if height[i] * (j - i) > largest_area:
                    largest_area = height[i] * (j - i)
                j -= 1
        return largest_area


# neetcode solution
# class Solution:
#     def maxArea(self, height):
#         l, r = 0, len(height) - 1
#         res = 0
        
#         while l < r:
#             res = max(res, min(height[l], height[r]) * (r - l))
#             if height[l] < height[r]:
#                 l += 1
#             elif height[r] <= height[l]:
#                 r -= 1
#         return res

class Test(unittest.TestCase):
    def test(self):
        s = Solution()
        
        input = [1,8,6,2,5,4,8,3,7]
        expected = 49
        output = s.maxArea(input)
        
        self.assertEqual(output, expected)
                
    def test2(self):
        s = Solution()
        
        input = [1,1]
        expected = 1
        output = s.maxArea(input)
        
        self.assertEqual(output, expected)


if __name__ == '__main__':
    unittest.main()
