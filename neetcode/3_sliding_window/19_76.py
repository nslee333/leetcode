
# my solution with GPT, we walked through the solution together.

# the trick is to shrink the window while the condition is met
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # s is original, t is substring

        t_count = {}

        for i in range(len(t)):
            t_count[t[i]] = t_count.get(t[i], 0) + 1
        
        l = 0
        sat_count = len(t_count.keys())
        res = float('inf')
        res_idea = []

        for r in range(len(s)):

            if s[r] in t_count:
                t_count[s[r]] = t_count[s[r]] - 1

                if t_count.get(s[r]) == 0:
                    sat_count -= 1


            while sat_count <= 0:
                if r - l + 1 < res:
                    res = r - l + 1
                    res_idea = [l, r+1]

                if s[l] in t_count:
                    t_count[s[l]] += 1
                    if t_count[s[l]] > 0:
                        sat_count += 1
                l += 1
            
            
        result = s[res_idea[0]: res_idea[1]] if res != float('inf') else ""

        return result
