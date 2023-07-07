package easy

/*
Given a sorted array of ints,

1. Find all unique nums.
2. Push the unique nums to the front
3. return the length of the sorted part


*/

func removeDuplicates(nums []int) int {
	if len(nums) == 0 {
		return 0
	}
	j := 1

	for i := 1; i < len(nums); i++ {
		if nums[i] != nums[i-1] {
			nums[j] = nums[i]
			j++
		}
	}

	return j
}
