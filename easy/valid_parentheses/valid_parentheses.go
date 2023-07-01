package easy

/*

	Given a string s containing just the characters () {} and []
	determine if the input is valid.

	 input is valid if:
	- Open brackets must be closed by the same type of brackets.
	- Open brackets must be closed in the correct order.
	- Every close bracket has a corresponding open bracket of the same type.

*/

var bracketStr = map[byte]byte{
	')': '(',
	'}': '{',
	']': '[',
}

func isValid(s string) bool {
	str := []byte(s)
	stack := make([]byte, 0)

	for _, element := range str {
		matchingOpening, isClosing := bracketStr[element]

		if !isClosing {
			stack = append(stack, element)
			continue
		}

		if len(stack) == 0 {
			return false
		}

		lastOpening := stack[len(stack)-1]
		stack = stack[:len(stack)-1]

		if lastOpening != matchingOpening {
			return false
		}

	}
	return len(stack) == 0
}
