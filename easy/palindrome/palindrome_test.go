package easy

import "testing"

func TestPalindrome(t *testing.T) {
	var cases = []struct {
		name     string
		input    int
		expected bool
	}{
		{name: "ex. 1", input: 121, expected: true},
		{name: "ex. 2", input: -121, expected: false},
		{name: "ex. 3", input: 10, expected: false},
		{name: "ex. 4", input: 1331, expected: true},
	}

	for _, c := range cases {
		t.Run(c.name, func(t *testing.T) {
			got := isPalindrome(c.input)
			if got != c.expected {
				t.Errorf("got %v, expected %v, input %v", got, c.expected, c.input)
			}
		})
	}
}
