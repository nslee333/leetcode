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
