package main

import (
	"reflect"
	"testing"
)

func TwoSumTableTest(t *testing.T) {
	t.Run("checks for correct output with example 1 input", func(t *testing.T) {
		nums := []int{2, 7, 11, 15}
		target := 9

		got := twoSum(nums, target)
		want := []int{0, 1}

		if !reflect.DeepEqual(got, want) {
			t.Errorf("got %v want %v", got, want)
		}
	})
}
