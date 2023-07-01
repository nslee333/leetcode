package easy

import (
	"reflect"
	"strconv"
	"strings"
)

/*

Given an integer `x`, return true if x is a palindrome, and false if otherwise.

Ex 1:
	Input: 121
	Output: True
	Explanation: 121 reads as 121 from left to right and from right to left.



*/

func isPalindrome(x int) bool {
	s := strconv.FormatInt(int64(x), 10)
	slice := strings.Split(s, "")
	target := make([]string, 0)

	for i := len(slice) - 1; i >= 0; i-- {
		target = append(target, slice[i])
	}

	if reflect.DeepEqual(slice, target) {
		return true
	} else {
		return false
	}
}
