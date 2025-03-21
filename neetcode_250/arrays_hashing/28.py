
# my brain is tired, so we're calling it.
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