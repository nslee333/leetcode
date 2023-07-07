package easy

import "testing"

func Test28(t *testing.T) {
	cases := []struct {
		testName      string
		inputHaystack string
		inputNeedle   string
		output        int
	}{
		{testName: "Ex.1", inputHaystack: "sadbutsad", inputNeedle: "sad", output: 0},
		{testName: "Ex.2", inputHaystack: "leetcode", inputNeedle: "leeto", output: -1},
	}

	for _, c := range cases {
		t.Run(c.testName, func(t *testing.T) {
			got := strStr(c.inputHaystack, c.inputNeedle)

			if got != c.output {
				t.Errorf("got %v, wanted %v", got, c.output)
			}
		})
	}
}
