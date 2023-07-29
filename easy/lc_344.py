# Leetcode 344

def reverseString(s):
        """
        Do not return anything, modify s in-place instead.
        """
        i = 0
        j = len(s)-1
        while i < j:
            temp = s[i]
            s[i] = s[j]
            s[j] = temp
            i += 1
            j -= 1