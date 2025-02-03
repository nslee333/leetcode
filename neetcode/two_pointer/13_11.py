
# neetcode solution, but less readable.
class Solution:
    def maxArea(self, height: List[int]) -> int:
        

        area = 0
        i, j = 0, len(height) - 1

        while i < j:
            guess = (j - i) * min(height[i], height[j])
            area = max(area, guess)

            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return area
                



# So, this is actually faster, pretty sure due to the guess bit, but less readable.
class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        area = 0
        
        i, j = 0, len(height) - 1

        while i < j:
            guess = (j - i) * min(height[i], height[j])
            
            if guess > area:
                area = guess

            if height[i] <= height[j]:
                i += 1
            elif height[i] > height[j]:
                j -= 1
        return area