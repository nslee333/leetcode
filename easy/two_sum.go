package easy

/*

Prompt:

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

*/

func twoSum(nums []int, target int) []int {
	result := make([]int, 0)

	for i := range nums {

		for j := range nums {

			if j < len(nums)-1 {

				if i == j {
					continue
				}

				if nums[i]+nums[j] == target {

					if i < j {
						res := append(result, i, j)
						return res

					} else {
						res := append(result, j, i)
						return res
					}

				} else {
					continue
				}
			}
		}

		if i == len(nums)-1 {
			return append(result, 0, 0)
		}
	}
	return result
}
