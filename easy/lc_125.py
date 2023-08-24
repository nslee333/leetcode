import string

class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = s.lower()
        s = filter(str.isalnum, s)
        s = list(s)

        i = 0
        j = len(s) - 1

        while i < j:
            if s[i] == s[j]:
                j -= 1
                i += 1
                continue
            if s[i] != s[j]:
                return False
        return True