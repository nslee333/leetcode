class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        items = set()

        for item in nums:
            if item in items:
                return True
            items.add(item)
        return False
