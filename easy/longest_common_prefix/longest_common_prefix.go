package easy

import "strings"

/*

Write a function to find the longest common prefix string amongst an array of strings

If no common prefix, return an empty string


*/

func longestCommonPrefix(input []string) string {
	result := ""

	for i := range input {
		pos := ""

		if i < len(input)-1 {
			first := strings.Split(input[i], "")
			second := strings.Split(input[i+1], "")

			if first[i] == second[i] {

			} else {
				break
			}

		}

	}

	return result
}
