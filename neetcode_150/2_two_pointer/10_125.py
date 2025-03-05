class Solution:
    def isPalindrome(self, s: str) -> bool:
        # filter out non-alphanumeric characters, convert to lowercase

        # check that the array is equal to itself backward.

        letters = ''.join(filter(str.isalnum, s)).lower()


        # [::-1] concise way to reverse the contents of an array
        return letters == letters[::-1]
    


class Solution:
    def isPalindrome(self, s: str) -> bool:
        # filter out non-alphanumeric characters, convert to lowercase

        # check that the array is equal to itself backward.


        letters = ''.join(filter(str.isalnum, s)).lower()

        p_1 = 0
        p_2 = len(letters) - 1

        while p_1 < p_2:
            if letters[p_1] == letters[p_2]:
                p_1 += 1
                p_2 -= 1
                if p_1 == p_2:
                    return True

            else:
                return False
        return True
    

# way cleaner, not really faster though
class Solution:
    def isPalindrome(self, s: str) -> bool:
        letters = ''.join(filter(str.isalnum, s)).lower()
        letters_copy = letters[::-1]

        return letters == letters_copy