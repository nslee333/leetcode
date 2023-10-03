class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        instances = {}
        res = 0
        
        for i in range(len(nums)):
            if instances.get(nums[i]):
                instances[nums[i]].append(i)
            else:
                instances[nums[i]] = [i]

        for value in instances.values():
            if len(value) > 1:
                res += (len(value)* (len(value) - 1)) // 2

        return res
