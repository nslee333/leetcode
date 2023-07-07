package easy

import "testing"

func TestLength(t *testing.T) {
	cases := []struct {
		testName string
		inputStr string
		expected int
	}{
		{testName: "Ex.1", inputStr: "Hello World", expected: 5},
		{testName: "Ex.2", inputStr: "   fly me   to   the moon  ", expected: 4},
		{testName: "Ex.3", inputStr: "luffy is still joyboy", expected: 6},
	}

	for _, c := range cases {
		t.Run(c.testName, func(t *testing.T) {
			got := lengthOfLastWord(c.inputStr)

			if got != c.expected {
				t.Errorf("got %v, expected %v,", got, c.expected)
			}
		})
	}
}
func TestLength2(t *testing.T) {
	cases := []struct {
		testName string
		inputStr string
		expected int
	}{
		{testName: "Ex.1", inputStr: "Hello World", expected: 5},
		{testName: "Ex.2", inputStr: "   fly me   to   the moon  ", expected: 4},
		{testName: "Ex.3", inputStr: "luffy is still joyboy", expected: 6},
	}

	for _, c := range cases {
		t.Run(c.testName, func(t *testing.T) {
			got := lengthOfLastWord2(c.inputStr)

			if got != c.expected {
				t.Errorf("got %v, expected %v,", got, c.expected)
			}
		})
	}
}
