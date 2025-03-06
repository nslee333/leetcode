# valid anagram

# optimal hash table solution


# linear time O(n + m) & constant space (since 26 letters in alphabet)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:     
        
        if len(s) != len(t):
            return False

        # init an  array of 26 characters (english alphabet)
        count = [0] * 26
        print(count)
        
        
        # as you iterate, add 1 for each character for s
        # subtract 1 for each char in t
        
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1
        
        # if anagrams, it'll even out to zero
        for item in count:
            if item > 0:
                return False

        return True


# simplist solution, log linear time O(n log n + m log m), linear space O(n + m)
# for sorted() (timsort)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:     
        return sorted(s) == sorted(t)