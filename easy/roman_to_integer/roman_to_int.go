package easy

import (
	"strings"
)

/*

	Given a roman numeral, convert it into an integer.

*/

func romanToInt(input string) int {
	m := make(map[string]int)

	m["I"] = 1
	m["V"] = 5
	m["X"] = 10
	m["L"] = 50
	m["C"] = 100
	m["D"] = 500
	m["M"] = 1000

	slice := strings.Split(input, "")
	result := 0

	for i := 0; i < len(slice); i++ {

		if i < len(slice)-1 && m[slice[i]] < m[slice[i+1]] {
			result -= m[slice[i]]

		} else {
			result += m[slice[i]]
		}
	}

	return result
}
