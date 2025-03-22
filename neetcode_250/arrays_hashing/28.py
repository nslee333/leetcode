# neetcode bruteforce solution, this is linear time O(N * m) and space is constant since we aren't using anything.
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        n, m = len(haystack), len(needle)
        for i in range(n - m + 1): # the range is the size of the window 
            j = 0
            while j < m: # grow j until it's the length if the needle
                if haystack[i + j] != needle[j]: # 
                    break
                j += 1
            if j == m:
                return i
        return -1
# my brain is tired, so we're calling it.

# this attempt was using a hashtable, but that's a flawed approach since hashtables in python are unordered.
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        needle = list(needle)

        window = {}
        for i, value in enumerate(haystack):
            if len(window) == len(needle):
                return
            window[i] = value

        
        for key, value in enumerate(haystack):
            if window.keys() == needle:
                print("HI!")
                return window.pop()
            else:
                window.pop()
                window.append()




# find the index of the first occurance in a string
# O(N) runtime, constant space
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)