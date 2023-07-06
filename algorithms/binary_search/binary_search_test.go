package algorithms

import (
	"fmt"
	"testing"
)

func TestBinarySearch(t *testing.T) {
	cases := []struct {
		testName string
		inputArr []string
		target   string
		expected int
	}{
		{testName: "Ex.1", inputArr: []string{"a", "b", "c", "d", "e", "f"}, target: "b", expected: 1},
		{testName: "Ex.2", inputArr: []string{"a", "b", "c", "d", "e", "f"}, target: "d", expected: 3},
		{testName: "Ex.3", inputArr: []string{"a", "b", "c", "d", "e", "f"}, target: "f", expected: 5},
		{testName: "Ex.4", inputArr: []string{"a", "b", "c", "d", "e", "f"}, target: "z", expected: -1},
	}

	for _, c := range cases {
		t.Run(c.testName, func(t *testing.T) {
			got, error := binary_search(c.inputArr, c.target)

			if error != nil {
				fmt.Println(c.testName, error)
			}

			if got != c.expected {
				t.Errorf("Got %v, expected %v, inputArr %v, target %v", got, c.expected, c.inputArr, c.target)
			}
		})
	}
}
