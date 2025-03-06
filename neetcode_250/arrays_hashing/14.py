# longest common prefix

# my solution
# linear time O(n * m) and linear space O(n)
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        
        
        # zip takes all chars at i and puts them into a tuple
        res = ""
        for chars in zip(*strs):
            # set is used for uniqueness, if more than one, then the prefix is broken
            if len(set(chars)) != 1:
                return res
            res += chars[0]
        return res
    
    
# neetcode vertical scanning sol, linear time & space
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""

        # scanning through first string
        for i in range(len(strs[0])):
            # for each string
            for s in strs:
                # if i is out of bounds or current string does not equal current prefix
                # return res 
                if i == len(s) or s[i] != strs[0][i]:
                    return res
            res += strs[0][i]
        
        return res