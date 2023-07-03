package easy

import "testing"

func TestRomanToInt(t *testing.T) {
	cases := []struct {
		testName string
		input    string
		output   int
	}{
		{testName: "Ex.1", input: "III", output: 3},
		{testName: "Ex.2", input: "LVIII", output: 58},
		{testName: "Ex.3", input: "MCMXCIV", output: 1994},
	}

	for _, c := range cases {
		t.Run(c.testName, func(t *testing.T) {
			got := romanToInt(c.input)
			want := c.output

			if got != want {
				t.Errorf("got %v, want %v, input %v", got, want, c.input)
			}
		})
	}

}
