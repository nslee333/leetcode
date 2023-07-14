import unittest

class Test(unittest.TestCase):
    def test(self):
        s = Solution()
        
        input = 0
        expected = 0
        output = s.function(input)
        
        self.assertEqual(output, expected)
                
    def test2(self):
        s = Solution()
        
        input = 0
        expected = 0
        output = s.function(input)
        
        self.assertEqual(output, expected)

if __name__ == '__main__':
    unittest.main()














package easy

import (
	"testing"
)

func TestRemove(t *testing.T) {
	cases := []struct {
		testName None
		input None
		expected  None
	}{
		{testName: "Ex.1", input: None, expected: None},
		{testName: "Ex.2", input: None, expected: None},
	}

	for _, c := range cases {
		t.Run(c.testName, func(t *testing.T) {
			got := removeElement(c.inputNums, c.inputVal)

			if got != c.expected {
				t.Errorf("got %v, expected %v,", got, c.expected)
			}
		})
	}
}
