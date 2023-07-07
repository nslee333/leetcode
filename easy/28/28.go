package easy

/*

! Find the index of the first occurance in a string

Given two strings needle and haystack, return the first occurance of needle in haystack or -1 if needle is not appart of haystack.



*/

func strStr(haystack, needle string) int {
	if len(needle) == 0 {
		return 0
	}

	if len(haystack) == 0 || len(haystack) < len(needle) {
		return -1
	}

	for i := 0; i < len(haystack)-len(needle)+1; i++ {
		if haystack[i:i+len(needle)] == needle {
			return i
		} else {
			continue
		}
	}

	return -1
}
