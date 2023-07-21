import unittest


"""

implement the myAtoi function, which converts a string into a 32-bit signed integer.

The algorithm for myAtoi(string s) is as follows:

Read in and ignore any leading whitespace.
Check if the next character (if not already at the end of the string) is '-' or '+'. 

- Read this character in if it is either. This determines if the final result is negative or positive respectively. 
- Assume the result is positive if neither is present.

- Read in next the characters until the next non-digit character or the end of the input is reached. The rest of the string is ignored.
- Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). 
- If no digits were read, then the integer is 0. 

- Change the sign as necessary (from step 2).
- If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then clamp the integer so that it remains in the range. 

- Specifically, integers less than -231 should be clamped to -231, and integers greater than 231 - 1 should be clamped to 231 - 1.
- Return the integer as the final result.

Note:

Only the space character ' ' is considered a whitespace character.
Do not ignore any characters other than the leading whitespace or the rest of the string after the digits.


"""





class Solution:
    def my_atoi(self, s:str) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        s = s.lstrip()
        
        sign = 1
        if s and (s[0] == '-' or [0] == '+'):
            if s[0] == '-':
                sign = -1
            s = s[1:]

        num = 0
        for char in s:
            if char.isdigit():
                num = num * 10 + int(char)
            else:
                break
        
        num *= sign
        
        if num > INT_MAX:
            return INT_MAX
        elif num < INT_MIN:
            return INT_MIN
        else:
            return num





class Test(unittest.TestCase):
    def test(self):
        s = Solution()
        
        input = "42"
        expected = 42
        output = s.my_atoi(input)
        
        self.assertEqual(output, expected)
                
    def test2(self):
        s = Solution()
        
        input = "   -42"
        expected = -42
        output = s.my_atoi(input)
        
        self.assertEqual(output, expected)

    def test3(self):
        s = Solution()
        
        input = "4193 with words"
        expected = 4193
        output = s.my_atoi(input)
        
        self.assertEqual(output, expected)

if __name__ == '__main__':
    unittest.main()