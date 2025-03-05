



# my solution: this one is much better, 19ms runtime, the sorting in the old one was horrid
#  this one is using a hashmap with a dynamic sliding window, 
# however this isn't as efficient as a fixed-size sliding window
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        s1_count = {}
        s2_count = {}


        for j in range(len(s1)):
            s1_count[s1[j]] = s1_count.get(s1[j], 0) + 1


        l = 0
        

        for r in range(len(s2)):
            while (r - l + 1) > len(s1):
                if s2_count.get(s2[l]) > 1:
                    s2_count[s2[l]] -= 1
                else:
                    s2_count.pop(s2[l])
                l += 1
            s2_count[s2[r]] = s2_count.get(s2[r], 0) + 1

            if s1_count == s2_count: return True

        return s1_count == s2_count


# my solution
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
                