
# one pass hash table -- linear time & space
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in table:
                return [table[diff], i]
            table[n] = i


# two pass hash table -- linear time & space
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = {}

        for i in range(len(nums)):
            table[nums[i]] = i

        for i in range(len(nums)):
            guess = target - nums[i]

            if table.get(guess):
                if i != table.get(guess):
                    return [i, table.get(guess)]
