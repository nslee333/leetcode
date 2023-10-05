# First solution
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maj = len(nums) // 2
        res = 0

        hash = {}

        for i in range(len(nums)):
            if not hash.get(nums[i]):
                hash[nums[i]] = 1
                continue
            hash[nums[i]] += 1

        for key, value in hash.items():
            if value > maj:
                res = key
        return res
       
# more optimized since it can exit early out of the loop:
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maj = len(nums) // 2
        res = 0

        hash = {}

        for i in range(len(nums)):
            if not hash.get(nums[i]):
                hash[nums[i]] = 1
            else:
                hash[nums[i]] += 1

            if hash.get(nums[i]) > maj:
                res = nums[i]
                break
        return res    
     
# Boyer-Moore voting algorithm solution, didn't come to this on my own.
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        element = nums[0]

        for num in nums:
            if num == element:
                count += 1
            else:
                if count:
                    count -= 1
                else:
                    element = num
                    count = 1
        return element
