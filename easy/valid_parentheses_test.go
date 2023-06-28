package easy

import "testing"

func TestIsValid(t *testing.T) {
	t.Run("Ex. 1", func(t *testing.T) {
		str := "()"
		want := true
		got := isValid(str)

		if got != want {
			t.Errorf("got %v, want %v, str %v ", got, want, str)
		}
	})
	t.Run("Ex. 2", func(t *testing.T) {
		str := "()[]{}"
		want := true
		got := isValid(str)

		if got != want {
			t.Errorf("got %v, want %v, str %v ", got, want, str)
		}
	})
	t.Run("Ex. 3", func(t *testing.T) {
		str := "(]"
		want := false
		got := isValid(str)

		if got != want {
			t.Errorf("got %v, want %v, str %v ", got, want, str)
		}
	})

	t.Run("single value returns false", func(t *testing.T) {
		str := "("
		want := false
		got := isValid(str)

		if got != want {
			t.Errorf("got %v, want %v, str %v ", got, want, str)
		}
	})
}
