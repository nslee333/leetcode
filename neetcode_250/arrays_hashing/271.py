

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