package easy

/*

Merge two lists in a one sorted list.

The list should be made by splicing together the nodes of the first two
lists.




*/

func Merge(input1, input2 []int) []int {
	result := make([]int, 0)
	for i := range input1 {
		result = append(result, input1[i])
	}

	for i := range input2 {
		result = append(result, input2[i])
	}

}
