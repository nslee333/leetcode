class Solution:
    def trap(self, height: List[int]) -> int:

        l, r = 0, len(height) - 1
        high = 0
        res = 0

        while l < r:
            if min(height[l], height[r]) > high:
                high = min(height[l], height[r])
                if height[l] < height[r]:
                    l += 1
                elif height[l] >= height[r]:
                    r -= 1
            elif height[l] < high:
                res += high - height[l]
                l += 1
            elif height[r] < high:
                res += high - height[r]
                r -= 1
            elif height[l] == high:
                l += 1
            elif height[r] == high:
                r -= 1

        return res
    
    
# class Solution:
#     def trap(self, height: List[int]) -> int:
#         if not height: return 0
        
        
#         l, r = 0, len(height) - 1
#         max_left, max_right = height[l], height[r]
        
#         while l < r:
#             if max_left < max_right:
#                 l += 1
#                 max_left = max(max_left, height[l])
#                 res += max_left - height[l]
                
#             else:
#                 r -= 1
#                 max_right = max(max_right, height[r])
#                 res += max_right - height[r]
#         return res