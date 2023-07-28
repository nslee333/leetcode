"""
Leetcode # 58 return the length of the last word

"""


def lengthOfLastWord(self, s: str) -> int:
    s = s.split()
    return len(s[-1])