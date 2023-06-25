package two_sum

import "testing"

func BenchmarkTwoSum(b *testing.B) {
	for i := 0; i < b.N; i++ {
		nums := []int{2, 7, 11, 15}
		target := 9

		twoSum(nums, target)
	}
}
