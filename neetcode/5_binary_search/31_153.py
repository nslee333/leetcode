
# this passes Leetcode, but it's supposed to be O(log n) runtime, this is O(n log n) runtime
class Solution:
    def findMin(self, nums: List[int]) -> int:
        nums = sorted(nums)
        return nums[0]