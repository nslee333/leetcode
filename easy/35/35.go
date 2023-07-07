package easy

/*

given a sorted array of distinct integers and a target value.
return the index if the target is found.
if not, return the index where it would be if inserted in order.

You must write an algorithm with o(log n) runtime complexity.

*/

func searchInsert(nums []int, target int) int {
	if target < nums[0] {
		return 0
	}

	if target > nums[len(nums)-1] {
		return len(nums)
	}

	low := 0
	high := len(nums) - 1

	for low <= high {
		mid := (low + high) / 2

		if nums[mid] == target {
			return mid

		} else if nums[mid] > target {
			high = mid - 1
			continue

		} else if nums[mid] < target {
			low = mid + 1
			continue

		}

	}
	return low

}
