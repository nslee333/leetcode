package easy

import (
	"testing"
)

func TestRemove(t *testing.T) {
	cases := []struct {
		testName  string
		inputNums []int
		target    int
		expected  int
	}{
		{testName: "Ex.1", inputNums: []int{1, 3, 5, 6}, target: 5, expected: 2},
		{testName: "Ex.2", inputNums: []int{1, 3, 5, 6}, target: 2, expected: 1},
		{testName: "Ex.3", inputNums: []int{1, 3, 5, 6}, target: 7, expected: 4},
	}

	for _, c := range cases {
		t.Run(c.testName, func(t *testing.T) {
			got := searchInsert(c.inputNums, c.target)

			if got != c.expected {
				t.Errorf("got %v, expected %v,", got, c.expected)
			}
		})
	}
}
