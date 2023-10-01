class Solution:
    def reverseWords(self, s: str) -> str:
        sp = s.split()
        res = []
        for i in range(len(sp)):
            spl = list(sp[i])
            spl.reverse()
            spl = ''.join(spl)
            res.append(spl)
            if i != len(sp) - 1:
                res.append(" ")
        
        res = ''.join(res)
        return res