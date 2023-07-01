package easy

import "strings"

/*

	Govem a string s containing just the characters () {} and []
	determine if the input is valid.

	 input is valid if:
	- Open brackets must be closed by the same type of brackets.
	- Open brackets must be closed in the correct order.
	- Every close bracket has a corresponding open bracket of the same type.

	* How to parse strings

	* 1. split string into a slice. X
	* 2. Loop over the slice. X
	* 3. Check that bracket is closed with a matching bracket, in the correct order.
		& Bracket is closed.
		& Bracket is closed + with the correct bracket.
		& In the correct order.



	* 4. If any of the conditions above are false, return false.
	* 5. Return true if string is valid.
	*

*/

// var closingToOpening = map[byte]byte{
// 	')': '(',
// 	'}': '{',
// 	']': '[',
// }

// func isValid(str string) bool {

// 	s := []byte(str)
// 	stack := make([]byte, 0)

// 	for _, ch := range s {
// 		matchingOpening, isClosing := closingToOpening[ch]

// 		if !isClosing {
// 			stack = append(stack, ch)
// 			continue
// 		}

// 		if len(stack) == 0 {
// 			return false
// 		}

// 		lastOpening := stack[len(stack)-1]
// 		stack = stack[:len(stack)-1]

// 		if lastOpening != matchingOpening {
// 			return false

// 		}
// 	}

// 	return len(stack) == 0

// }

func isValid(s string) bool {

	var stack []string
	slice := strings.Split(s, "")

	for i := range slice {
		if slice[i] == `(` || slice[i] == `{` || slice[i] == `[` {
			stack = append(stack, slice[i])

		} else if slice[i] == `)` || slice[i] == `}` || slice[i] == `]` {
			if len(stack) != 0 {

				if stack[len(stack)-1] == `(` || stack[len(stack)-1] == `{` || stack[len(stack)-1] == `[` {

					if stack[len(stack)-1] == `(` && stack[i] == `)` {
						if len(stack) != 0 {
							stack = stack[:len(stack)-1]

						} else {
							return false
						}

					} else if stack[len(stack)-1] == `{` && stack[i] == `}` {
						if len(stack) != 0 {
							stack = stack[:len(stack)-1]

						} else {
							return false
						}

					} else if stack[len(stack)-1] == `[` && stack[i] == `]` {
						if len(stack) != 0 {
							stack = stack[:len(stack)-1]

						} else {
							return false
						}

					}

				} else {
					return false
				}

			} else {
				return false
			}
		}

	}

	return len(stack) == 0
}

// & (] returns true - because any opening bracket can match and opening bracket.
