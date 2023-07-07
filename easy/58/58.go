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
	str := strings.Split(s, "")

	lastWord := make([]string, 0)

	for i := len(str) - 1; i >= 0; i-- {

		if str[i] == ` ` && len(lastWord) < 1 {
			continue

		} else if str[i] == ` ` && len(lastWord) >= 1 {
			break

		} else if str[i] != ` ` {
			lastWord = append(lastWord, str[i])
		}
	}
	return len(lastWord)
}
