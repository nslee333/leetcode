package easy

import (
	"fmt"
	"strings"
)

/*

Write a function to find the longest common prefix string amongst an array of strings

If no common prefix, return an empty string


*/

// &

func longestCommonPrefix(input []string) string {
	result := ""

	for i := range input {
		temp := make([]string, 0)

		if i < len(input)-1 {
			first := strings.Split(input[i], "")
			second := strings.Split(input[i+1], "")

			if 0 < len(first)-1 && 0 < len(second)-1 && first[0] == second[0] {
				for j := range first {

					if j < len(input)-1 && first[j] == second[j] {
						temp = append(temp, first[j])
						continue

					} else {
						break
					}

				}

			}

			result = strings.Join(temp, "")
		} else if len(input) == 1 {
			result = input[i]
		} else if i < len(input)-1 && input[i] != input[i+1] {
			result = ""
		}
		return result
	}

	fmt.Println(result)
	return result
}
