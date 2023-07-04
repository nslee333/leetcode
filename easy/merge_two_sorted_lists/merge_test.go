package easy

import (
	"reflect"
	"testing"
)

func TestMerge(t *testing.T) {
	cases := []struct {
		testName string
		input1   []int
		input2   []int
		expected []int
	}{
		{testName: "Ex.1", input1: []int{1, 2, 4}, input2: []int{1, 3, 4}, expected: []int{1, 1, 2, 3, 4, 4}},
		{testName: "Ex.2", input1: []int{}, input2: []int{}, expected: []int{}},
		{testName: "Ex.1", input1: []int{}, input2: []int{0}, expected: []int{0}},
	}

	for _, c := range cases {
		t.Run(c.testName, func(t *testing.T) {
			result := Merge(c.input1, c.input2)

			if !reflect.DeepEqual(result, c.expected) {
				t.Errorf("result %v, expected %v, input 1 %v, input 2 %v", result, c.expected, c.input1, c.input2)
			}
		})
	}
}
