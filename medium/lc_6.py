import unittest


"""
Leetcode #6

Zigzag conversion

The string "PAYPALISHIRING" is written as a zig zag on a given number of rows like this:
write the code that will take a string and make this conversion given a number of rows

input_s = "PAYPALISHIRING"
input_rows = 3

input_rows = 5

PH ASI YIR PLIG AN

P     H        
A   S I        
Y  I  R        
P L   I G      
A     N       

expected = PAHN APLSIIG YIR
output =   PAHNAPLSIIGYIR

P   A   H   N
A P L S I I G
Y   I   R


& can we do something with the length of the string
grid = len_rows and len(string)

x rows of characters down

PAYPALISHIRING => string that can b

arr = [
    []
]
    str = list(string)

for item in str:
    count = 0
    if count < len(rows):
        going down
        arr[count][0] = item
        count++
    elif count = len(rows):
        count -= 1
        arr[count][1.2.3.4.5] = item
     




[
    [p      h        ]
    [a    s i        ]
    [y  i   r        ]
    [p l    i g      ]
    [a      n        ]
]


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