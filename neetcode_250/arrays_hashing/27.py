
# neetcode solution, linear time and constant space
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k




# my solution, quadratic time, constant space because removing an arbitary index from a list in python
# takes linear time in worst case, making the solution quadratic time O(N^2)
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        i = 0
        while i < len(nums):
            if nums[i] == val:
                nums.pop(i)
            else:
                i += 1
        return len(nums)