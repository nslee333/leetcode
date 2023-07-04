package easy

import "sort"

/*

Write a function to find the longest common prefix string amongst an array of strings

If no common prefix, return an empty string


*/

// &

func longestCommonPrefix(input []string) string {
	if len(input) == 1 {
		return input[0]
	}

	sort.Strings(input)

	l := len(input)
	for i := range input[0] {
		if input[0][i] != input[l-1][i] {
			return input[0][:i]
		}
	}

	return input[0]
}
