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
		& Bracket is closed with the correct bracket.
		& In the correct order.



	* 4. If any of the conditions above are false, return false.
	* 5. Return true if string is valid.
	*

*/

func isValid(s string) bool {

	result := false
	slice := strings.Split(s, "")

	// If an odd number of elements, return false
	if len(slice)%3 != 1 {
		return result
	}

	for i := range slice {
		check := slice[i]
		//

		for j := 0; j < len(slice); j++ {
			if slice[j] == check {
				result = true
			}
		}

	}
	return result
}
