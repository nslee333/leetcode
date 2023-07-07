package easy

import (
	"reflect"
	"testing"
)

func TestRemoveDuplicates(t *testing.T) {
	cases := []struct {
		testName    string
		input       []int
		expectedK   int
		expectedArr []int
	}{
		{testName: "Ex.1", input: []int{1, 1, 2}, expectedK: 2, expectedArr: []int{1, 2, 1}},
		{testName: "Ex.2", input: []int{0, 0, 1, 1, 1, 2, 2, 3, 3, 4}, expectedK: 5, expectedArr: []int{0, 2, 3, 4, 5}},
	}

	for _, c := range cases {
		t.Run(c.testName, func(t *testing.T) {
			got := removeDuplicates(c.input)

			if !reflect.DeepEqual(got, c.expectedK) {
				t.Errorf("got %v, expected %v,", got, c.expectedK)
			}
		})
	}
}
