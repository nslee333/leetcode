
# neetcode solution,
# linear time and space

# encoder: at the beginning of each string, append length and # as a delimiter

# decoder: look for length# delimiter, find that slice, append to array
#          and return array
class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        
        return res


    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        print(s)

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            print(length)
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j
        return res
    
    
# I was able to make this work completely on accident
# linear space & time
class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for item in strs:
            res += (item + "\u000c")
        return res

    def decode(self, s: str) -> List[str]:
        res = s.split("\u000c")
        
        # this was a hacky fix to remove my delimter, and it solved some hard edge cases on accident
        if res[-1] == '':
            res = res[:len(res) - 1]
        
        return res