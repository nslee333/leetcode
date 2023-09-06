def ll(s, k):
    # res = 0
    # l = 0
    # _l = list()
    # _k = k
    
    # for r in range(len(s)):
    #     print(res)
    #     res = max(res, len(_l))
    #     if not _l or s[r] == _l[-1]:
    #         _l.append(s[r])
    #     elif s[r] != _l[-1] and _k != 0:
    #         _k -= 1
    #         _l.append(_l[-1])
    #     elif s[r] != _l[-1]:
    #         _l.clear()
    #         _l.append(s[r])
    #         l = r
    #         _k = k
        
    # return res
    
    # ^ neetcode solution 1
    # count = {}
    # res = 0

    # l = 0
    # for r in range(len(s)):
    #     count[s[r]] = 1 + count.get(s[r], 0)
        
    #     while (r - l + 1) - max(count.values()) > k:
    #         count[s[l]] -= 1
    #         l += 1
        
    #     res = max(res, r - l + 1)
    # return res

    # ^ neetcode solution 2
    
    # class Solution:
    #     def characterReplacement(self, s: str, k: int) -> int:
    #         count = {}
    #         res = 0

    #         l = 0
    #         maxf = 0 
    #         for r in range(len(s)):
    #             count[s[r]] = 1 + count.get(s[r], 0)
    #             maxf = max(maxf, count[s[r]])
                
    #             while (r - l + 1) - maxf > k:
    #                 count[s[l]] -= 1
    #                 l += 1
                
    #             res = max(res, r - l + 1)
    #         return res

    