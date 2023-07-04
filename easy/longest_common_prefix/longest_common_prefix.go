package easy

import (
	"fmt"
	"strings"
)

/*

Write a function to find the longest common prefix string amongst an array of strings

If no common prefix, return an empty string


*/

func longestCommonPrefix(input []string) string {
	pos := make([]string, 0)

	f := strings.Split(input[0], "")
	result := f[0]

	for i := range input {
		temp := input[i]
		if i < len(input)-1 {
			if input[i+1] == temp {

				// & set temp = input[0] -> compare to input[1]
				// & if true - continue and append.
				// & if false, return temp as result
			}

		}
		result += temp
	}

	result = strings.Join(pos, "")
	fmt.Println(result)
	return result
}
