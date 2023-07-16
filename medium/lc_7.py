import unittest


"""
Given a signed 32-bit integer x, return x with its digits reversed. 
If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).


"""


class Solution:
    def reverse(self, x: int) -> int:
        
        num_string = ""

        string_x = str(x)
        
        i = len(string_x)-1
        while i >= 0:
            if string_x[i] == "-":
                num_string = "-" + num_string
                i -= 1
            else:  
                num_string += string_x[i]
                i -= 1
                
            
        result = int(num_string)
        
        if result < -2**31 or result > (2**31 - 1):
            return 0
        
        
        return result
    
    # def reverse(self, x: int) -> int:
    #     is_negative = False

    #     if x < 0:
    #         is_negative = True
    #         x = abs(x)


    #     result = 0

    #     while x != 0:
    #         digit = x % 10
    #         x //= 10
            
    #         result = result * 10 + digit
            
    #         if result < -(2**31) or result > (2**31)-1:
    #             result = 0
            
            

    #     if is_negative:
    #         result *= -1

    #     return result
        



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
        
    def test4(self):
        s = Solution()
        
        input = 1534236469
        expected = 0
        output = s.reverse(input)
        
        self.assertEqual(output, expected)
        
    def test4(self):
        s = Solution()
        
        input = -2147483412
        expected = -2143847412
        output = s.reverse(input)
        
        self.assertEqual(output, expected)
    def test5(self):
        s = Solution()
        
        input = -2147483412
        expected = -2143847412
        output = s.reverse(input)
        
        self.assertEqual(output, expected)
        
    def test6(self):
        s = Solution()
        
        input = 1534236469
        expected = 0
        output = s.reverse(input)
        
        self.assertEqual(output, expected)

if __name__ == '__main__':
    unittest.main()

