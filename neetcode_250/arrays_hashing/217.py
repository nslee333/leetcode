
# linear time O(N), because we loop through each element
# space is linear as well, since the worst case is that we have to store N elements
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        items = set()

        for item in nums:
            if item in items:
                return True
            items.add(item)
        return False
