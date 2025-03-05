# On time and ON space
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        seen = {}
        total = 0
        i = 0
        max_freq = 0

        for j in range(len(s)):

            seen[s[j]] = 1 + seen.get(s[j], 0)
            max_freq = max(max_freq, seen[s[j]])
                       

            while (j - i + 1) - max_freq > k:
                seen[s[i]] -= 1
                i += 1
        
            total = max(total, j - i + 1)
        return total