class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hash = {}

        for i in range(len(nums)):
            if hash.get(nums[i]):
                return nums[i]
            else:
                hash[nums[i]] = 1
        
