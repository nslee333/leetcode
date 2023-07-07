package easy

import (
	"testing"
)

func TestAdd(t *testing.T) {
	cases := []struct {
		testName string
		inputA   string
		inputB   string
		output   string
	}{
		{testName: "Ex.1", inputA: "11", inputB: "1", output: "10101"},
		{testName: "Ex.2", inputA: "1010", inputB: "1011", output: "10101"},
	}

	for _, c := range cases {
		t.Run(c.testName, func(t *testing.T) {
			got := addBinary(c.inputA, c.inputB)

			if got != c.output {
				t.Errorf("got %v, expected %v, inputA %v, inputB %v", got, c.output, c.inputA, c.inputB)
			}
		})
	}
}
