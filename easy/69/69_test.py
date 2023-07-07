sixNine = __import__('69')
import unittest

class TestSolution(unittest.TestCase):
    def runTest(self):
        input_x = 4
        output = 2
        got = Solution.mySqrt(input_x)
        
        self.assertEqual(got, output, f"got {got}, output{output}, input_x {input_x}")