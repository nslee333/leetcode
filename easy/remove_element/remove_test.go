package easy

import (
	"testing"
)

func TestRemove(t *testing.T) {
	cases := []struct {
		testName  string
		inputNums []int
		inputVal  int
		expected  int
	}{
		{testName: "Ex.1", inputNums: []int{3, 2, 2, 3}, inputVal: 3, expected: 2},
		{testName: "Ex.2", inputNums: []int{0, 1, 2, 2, 3, 0, 4, 2}, inputVal: 2, expected: 5},
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
