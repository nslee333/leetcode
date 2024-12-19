
"""
    Given two strings s and t, return true if t is an anagram
    of s, and false otherwise.
"""


# Elegant, faster & more storage efficient 
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)



# Brute force
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:     
        if len(s) != len(t):
            return False

        s = sorted(list(s))
        t = sorted(list(t))

        # brute force
        for s_i in range(len(s)):
            if s[s_i] != t[s_i]:
                return False
        return True
    
# bit more complicated solution, the funny part is that this is slower than above
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:     
        if len(s) != len(t):
            return False

        s = list(s)
        t = list(t)

        hash_table = {}

        for s_i in range(len(s)):
            if hash_table.get(s[s_i]):
                hash_table[s[s_i]] += 1
            else:
                hash_table[s[s_i]] = 1

        for t_i in range(len(t)):
            if hash_table.get(t[t_i]) != None and hash_table.get(t[t_i]) > 0:
                hash_table[t[t_i]] -= 1
            elif hash_table.get(t[t_i]) == None or hash_table.get(t[t_i]) <= 0:
                return False

        for value in hash_table.values():
            if value != 0:
                print('2')
                return False
        return True