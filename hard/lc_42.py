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
    
    
