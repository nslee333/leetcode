package easy

import (
	"fmt"
	"strconv"
)

/*

Given two binary strings a and b, return their sum as a binary string

*/

func addBinary(a, b string) string {
	result := ""
	carry := 0

	i, j := len(a)-1, len(b)-1

	for i >= 0 || j >= 0 {
		sum := carry

		if i >= 0 {
			sum += int(a[i] - '0')
			i--
		}

		if j >= 0 {
			fmt.Println(int(b[j] - '0'))
			sum += int(b[j] - '0')
			j--
		}

		result = strconv.Itoa(sum%2) + result
		carry = sum / 2
	}

	if carry > 0 {
		result = strconv.Itoa(carry) + result
	}
	return result
}
