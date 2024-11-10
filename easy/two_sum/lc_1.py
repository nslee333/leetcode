class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hashmap = {}


        for index, num in enumerate(nums):
            compliment = target - num

            if compliment in hashmap:
                return [hashmap[compliment], index]
            hashmap[num] = index

        return []