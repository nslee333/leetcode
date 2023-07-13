import unittest


"""
Leetcode #6

Zigzag conversion

The string "PAYPALISHIRING" is written as a zig zag on a given number of rows like this:

P   A   H   N
A P L S I I G
Y   I   R

write the code that will take a string anad make this conversion given a number of rows



"""





class Solution:
    def convert(self, s: str, numRows: int) -> str:
        return ""





class Test(unittest.TestCase):
    def test(self):
        s = Solution()
        
        input_s = "PAYPALISHIRING"
        input_rows = 3
        expected = "PAHNAPLSIIGYIR"
        output = s.convert(input_s, input_rows)
        
        self.assertEqual(output, expected)
                
    def test2(self):
        s = Solution()
        
        input_s= "PAYPALISHIRING"
        input_rows = 4
        expected = "PINALSIGYAHRPI"
        output = s.convert(input_s, input_rows)
        
        self.assertEqual(output, expected)
        
    def test3(self):
        s = Solution()
        
        input_s= "A"
        input_rows = 1
        expected = "A"
        output = s.convert(input_s, input_rows)
        
        self.assertEqual(output, expected)

if __name__ == '__main__':
    unittest.main()