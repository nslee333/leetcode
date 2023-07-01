package easy

import "testing"

func TestIsValid(t *testing.T) {

	cases := []struct {
		str  string
		want bool
	}{
		{str: "()", want: true},
		{str: "(())", want: true},
		{str: "()())", want: false},
		{str: "(())()))", want: false},
		{str: "()[]{}", want: true},
		{str: "(]", want: false},
		{str: "(", want: false},
	}

	for _, c := range cases {
		got := isValid(c.str)
		want := c.want

		if got != want {
			t.Errorf("got %v, want %v, str %v", got, want, c.str)
		}
	}
}
