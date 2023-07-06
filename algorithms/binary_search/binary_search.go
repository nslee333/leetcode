package algorithms

import (
	"errors"
)

/*

binary search written in go

*/

func binary_search(inputArr []string, target string) (int, error) {
	low := 0
	high := len(inputArr) - 1

	for low <= high {
		mid := (low + high) / 2
		guess := inputArr[mid]

		if guess == target {
			return mid, nil

		} else if guess > target {

			high = mid - 1
			continue
		} else {

			low = mid + 1
			continue
		}
	}
	return -1, errors.New("target is not in array")
}
