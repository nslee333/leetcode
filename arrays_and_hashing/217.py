"""
    Given an integer array nums, 
    return true if any value appears at least twice in the array,
    and return false if every element is distinct.

"""



class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        item_set = set()

        for item in nums:
            if item in item_set:
                return True
            item_set.add(item)
        return False
