package easy

import (
	"strings"
)

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

func isValid(s string) bool {

	var stack []string
	slice := strings.Split(s, "")

	for i := range slice {
		if slice[i] == `(` {
			stack = append(stack, slice[i])

		} else if slice[i] == `{` {
			stack = append(stack, slice[i])

		} else if slice[i] == `[` {
			stack = append(stack, slice[i])

		} else if slice[i] == `)` {

			if stack[0] == `(` {
				// fmt.Println(len(stack))
				// fmt.Println(stack[0])
				// fmt.Println(stack[1:])
				copy(stack[i:], stack[i+1:])
				stack = stack[:len(stack)-1]

				// & Stopped at trying to get a version of .pop working.
			}

		} else if slice[i] == `}` {

			if stack[0] == `{` {
				stack = stack[0:]
			}

		} else if slice[i] == `]` {

			if stack[0] == `[` {
				stack = stack[1:]
			}
		}
	}

	if len(stack) == 0 {
		return true
	} else {
		return false
	}

}
