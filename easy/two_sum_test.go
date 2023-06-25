package two_sum

import (
	"reflect"
	"testing"
)

func TestTwoSum(t *testing.T) {
	t.Run("checks for correct output with example 1 input", func(t *testing.T) {
		nums := []int{2, 7, 11, 15}
		target := 9

		got := twoSum(nums, target)
		want := []int{0, 1}

		if !reflect.DeepEqual(got, want) {
			t.Errorf("got %v want %v", got, want)
		}
	})

	t.Run("checks for correct output with example 2 input", func(t *testing.T) {
		nums := []int{3, 2, 4}
		target := 6

		got := twoSum(nums, target)
		want := []int{1, 2}

		if !reflect.DeepEqual(got, want) {
			t.Errorf("got %v want %v", got, want)
		}
	})

	t.Run("checks for correct output with example 3 input", func(t *testing.T) {
		nums := []int{3, 3}
		target := 6

		got := twoSum(nums, target)
		want := []int{0, 1}

		if !reflect.DeepEqual(got, want) {
			t.Errorf("got %v want %v", got, want)
		}
	})

	t.Run("checks for correct output with duplicate ints in input", func(t *testing.T) {
		nums := []int{3, 3, 3, 3, 3, 1}
		target := 6

		got := twoSum(nums, target)
		want := []int{0, 1}

		if !reflect.DeepEqual(got, want) {
			t.Errorf("got %v want %v", got, want)
		}
	})

	t.Run("checks for proper panic error handling by giving nums and target that don't match", func(t *testing.T) {
		nums := []int{3, 3, 3, 3, 3}
		target := 1

		got := twoSum(nums, target)
		want := []int{0, 1}

		if !reflect.DeepEqual(got, want) {
			t.Errorf("got %v want %v", got, want)
		}
	})
}
