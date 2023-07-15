import unittest


class Solution:
    def reverse(self, x: int) -> int:
        return 0













class Test(unittest.TestCase):
    def test(self):
        s = Solution()
        
        input = 123
        expected = 321
        output = s.reverse(input)
        
        self.assertEqual(output, expected)
                
    def test2(self):
        s = Solution()
        
        input = -123
        expected = -321
        output = s.reverse(input)
        
        self.assertEqual(output, expected)
        
    def test3(self):
        s = Solution()
        
        input = 120
        expected = 21
        output = s.reverse(input)
        
        self.assertEqual(output, expected)

if __name__ == '__main__':
    unittest.main()

