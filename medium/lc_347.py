import unittest

class Solution:
    def top_k_frequent(self, nums, k):
        return []





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