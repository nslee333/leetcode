package easy

import (
	"strings"
)

func lengthOfLastWord(s string) int {
	trimmedStr := strings.Trim(s, " ")
	str := strings.Split(trimmedStr, " ")
	return len((str[len(str)-1]))
}
