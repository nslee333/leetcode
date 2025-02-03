class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # originally my idea was to iterate once to get the product of the array, 
        # 
        # then dividing the product by nums[i], appending to the array, but that wasn't accepted according to leetcode.
        
        return []        


# neetcode solution
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i] 

        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res  