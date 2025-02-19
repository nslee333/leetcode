
# Neetcode solution
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l, r = 0, len(nums) - 1
        
        split = int(len(nums) / 2)

        while l <= r:
            # because r + l can lead to overflow
            split = l + ((r - l) // 2)

            if nums[split] < target:
                l = split + 1

            elif nums[split] > target:
                r = split - 1

            else:
                return split

        return -1


# my solution
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        res = -1

        split = int(len(nums) / 2)

        while l <= r:
            split = int((r + l) / 2)

            if nums[split] < target:
                l = split + 1

            elif nums[split] > target:
                r = split - 1

            elif nums[split] == target:
                return split

        return res
