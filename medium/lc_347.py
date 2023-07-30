import unittest

"""
Leetcode 347

Given an integer array nums and an integer k, return the k most frequent elements. 

You may return the answer in any order.


"""

class Solution:
    def top_k_frequent(self, nums, k):
        count = {}
        freq = [[] for i in range(len(nums)+1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)

        for n, c in count.items():
            freq[c].append(n)

        res = []

        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res






class Test(unittest.TestCase):
    def test(self):
        s = Solution()
        
        input = [1,1,1,2,2,3]
        input_k = 2
        expected = [1,2]
        output = s.top_k_frequent(input, input_k)
        
        self.assertEqual(output, expected)
                
    def test2(self):
        s = Solution()
        
        input = [1]
        input_k = 1
        expected = [1]
        output = s.top_k_frequent(input, input_k)
        
        self.assertEqual(output, expected)

if __name__ == '__main__':
    unittest.main()