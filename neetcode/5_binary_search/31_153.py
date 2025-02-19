
# neetcode solution, O(log n) time, O(1) space
class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums) - 1

        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            
            m = (l + r) // 2
            res = min(res, nums[m])
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        return res

# more elegant kinda
class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        l, r = 0, len(nums) - 1
        res = float('inf')

        while l <= r:
            mid = (l + r) // 2
            
            mid_guess = nums[mid]
            left_guess = nums[l]
            right_guess = nums[r]

            if left_guess < right_guess:
                res = min(res, left_guess)
                break
            
            res = min(res,mid_guess)
            
            if mid_guess >= left_guess:
                l = mid + 1
            else:
                r = mid - 1

        return res

# my working solution, with neetcode pivot idea, not super elegant
class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        l, r = 0, len(nums) - 1
        res = float('inf')

        while l <= r:
            mid = l + (r - l) // 2
            
            mid_guess = nums[mid]
            left_guess = nums[l]
            right_guess = nums[r]
            
            print(left_guess, mid_guess)
            
            if mid_guess >= left_guess:
                res = min(res, left_guess)
                l = mid + 1
                
            else:
                res = min(res, right_guess)
                r = mid - 1
            res = min(res,mid_guess)
                
        
        return res

# this passes Leetcode, but it's supposed to be O(log n) runtime, this is O(n log n) runtime
class Solution:
    def findMin(self, nums: List[int]) -> int:
        nums = sorted(nums)
        return nums[0]