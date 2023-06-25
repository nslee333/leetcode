package two_sum

// Prompt:

// Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

// You may assume that each input would have exactly one solution, and you may not use the same element twice.

// You can return the answer in any order.

// Input: nums = [2,7,11,15], target = 9
// Output: [0,1]
// Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

func twoSum(nums []int, target int) []int {
	result := make([]int, 0)

	for i := range nums {

		num := nums[i]
		num2 := nums[i+1]

		if num+num2 == target {
			return append(result, num, num2)
		} else {
			continue
		}
	}

	return result
}
