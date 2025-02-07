# dog slow LOL, like 3045MS 😅 can't believe it passed LMAO
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_sorted = sorted(s1)

        l = 0

        for r in range(len(s2)):
            if len(s1) == (r - l + 1):
                if sorted(s2[l:r+1]) == s1_sorted:
                    return True
                l += 1
        return False
                