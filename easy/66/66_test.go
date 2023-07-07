package easy

import (
	"reflect"
	"testing"
)

func TestLength(t *testing.T) {
	cases := []struct {
		testName string
		nums     []int
		expected []int
	}{
		{testName: "Ex.1", nums: []int{1, 2, 3}, expected: []int{1, 2, 4}},
		{testName: "Ex.2", nums: []int{4, 3, 2, 1}, expected: []int{4, 3, 2, 2}},
		{testName: "Ex.3", nums: []int{9}, expected: []int{1, 0}},
	}

	for _, c := range cases {
		t.Run(c.testName, func(t *testing.T) {
			got := plusOne(c.nums)

			if !reflect.DeepEqual(got, c.expected) {
				t.Errorf("got %v, expected %v,", got, c.expected)
			}
		})
	}
}
