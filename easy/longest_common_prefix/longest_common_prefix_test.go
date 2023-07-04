package easy

import "testing"

func TestLongestCommonPrefix(t *testing.T) {

	cases := []struct {
		testName string
		input    []string
		output   string
	}{
		{testName: "Ex.1", input: []string{"flower", "flow", "flight"}, output: "fl"},
		{testName: "Ex.2", input: []string{"dog", "racecar", "car"}, output: ""},
		{testName: "Ex.3", input: []string{"a"}, output: "a"},
		{testName: "Ex.4", input: []string{"reflower", "flow", "flight"}, output: ""},
	}

	for _, c := range cases {
		t.Run(c.testName, func(t *testing.T) {
			got := longestCommonPrefix(c.input)
			want := c.output

			if got != want {
				t.Errorf("got `%v`, want %v, input %v", got, want, c.input)
			}
		})
	}
}
