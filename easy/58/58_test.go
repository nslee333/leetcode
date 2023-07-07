package easy

import "testing"

func TestRemove(t *testing.T) {
	cases := []struct {
		testName string
		inputStr string
		expected int
	}{
		{testName: "Ex.1", inputStr: "", expected: 2},
		{testName: "Ex.2", inputStr: "", expected: 1},
		{testName: "Ex.3", inputStr: "", expected: 4},
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
