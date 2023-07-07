package easy

import (
	"strings"
)

func lengthOfLastWord(s string) int {
	trimmedStr := strings.Trim(s, " ")
	str := strings.Split(trimmedStr, " ")
	return len((str[len(str)-1]))
}

func lengthOfLastWord2(s string) int {
	return 0
}
