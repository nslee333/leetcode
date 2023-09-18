class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        # 1. Find the largest value in the window.

        # 2. Build and return an array of largest window values

        # intuition:
        # Looking in the window, we loop through the window, and we push the largest number

        # l = 0
        # r = l
        
        res = []

        for l in range(len(nums)):
            temp_max = nums[l] 
            r = l
            while (r - l) < k and r < len(nums):
                temp_max = max(nums[r], temp_max)
                r += 1
            if (r - l) == k:
                res.append(temp_max)
        return res
            
        

        