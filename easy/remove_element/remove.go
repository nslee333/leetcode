package easy

func removeElement(nums []int, val int) int {
	if len(nums) == 0 {
		return 0
	}

	j := 0
	for i := range nums {
		if nums[i] != val {
			nums[j] = nums[i]
			j++
		}
	}
	return j
}
