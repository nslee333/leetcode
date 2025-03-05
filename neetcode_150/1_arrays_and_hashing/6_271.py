# encode and decode strings


# my broken attempt
class Solution:

    def encode(self, strs: List[str]) -> str:

        # split by whitespace

        # if it's 0 what do we do?
            # return ""
        # if it's 1 what do we do?
            # return item[i]

        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]


        res = ""
        for item in strs:
            res += item + " "
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        if len(s) == 0:
            return res
        if len(s) >= 1:
            return s.split()
  
# second attempt   
class Solution:

    def encode(self, strs: List[str]) -> str:

        # split by whitespace

        # if it's 0 what do we do?
            # return ""
        # if it's 1 what do we do?
            # return item[i]

        if not strs:
            return ""


        res = ""
        for item in strs:
            length = len(item)
            res += item + f"{length}#"
        return res

    def decode(self, s: str) -> List[str]:
        return []
        # res = []
        # if len(s) == 0:
        #     return []
        
        # strings = list(str)

        # for i in range(strings):
        #     if i < len(strings) - 1:
                    
# solution
class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res


    def decode(self, s: str) -> List[str]:
        res, i = [], 0
        
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            res.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length
            
        return res
