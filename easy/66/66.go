package easy

/*

Plus one

You are given a large integer represented as an integer array digits,
where each digits[i] is the ith digit of the integer.

The digits are ordered from most significant to least significant in left-to-right order.
The large integer does not contain any leading 0's.


*/

func plusOne(digits []int) []int {
	for i := len(digits) - 1; i >= 0; i-- {

		if digits[i] == 9 && i == 0 {
			digits[i] = 1
			digits = append(digits, 0)
			continue

		} else if digits[i] != 9 {
			digits[i] += 1
			return digits

		} else if digits[i] == 9 {
			digits[i] = 0
			continue
		}
	}

	return digits

}
