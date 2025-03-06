# valid anagram


# simplist solution, log linear time O(n log n + m log m), linear space O(n + m)
# for sorted() (timsort)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:     
        return sorted(s) == sorted(t)