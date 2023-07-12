"""
Given a string s, find the length of the longest substring without repeating characters


"""

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
    