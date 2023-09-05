"""
Given a string s, find the length of the longest substring without repeating characters


"""
class Solution:
    def lengthOfLongestSubstring(s: str) -> int:
        n = len(s)
        start = 0
        end = 0
        maxLen = 0
        seen = set()

        while end < n:
            if s[end] not in seen:
                seen.add(s[end])
                end += 1
                maxLen = max(maxLen, end - start)
            else:
                seen.remove(s[start])
                start += 1
        return maxLen


# ^ Neetcode solution

# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         charSet = set()
#         l = 0
#         res = 0

#         for r in range(len(s)):
#             while s[r] in charSet:
#                 charSet.remove(s[l])
#                 l += 1
#             charSet.add(s[r])
#             res = max(res, r - l + 1)
#         return res