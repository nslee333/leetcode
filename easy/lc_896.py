# working python solution O(n) runtime solution

class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        i, j = 0, len(nums) - 1
        
        if nums[i] < nums[j]:
            prev = float('-infinity')

            for i in range(len(nums)):

                if nums[i] >= prev:
                    prev = nums[i]
                    continue

                elif nums[i] < prev:
                    return False
            return True

        else:
            prev = float('infinity')

            for i in range(len(nums)):
                print(i)
                if nums[i] <= prev:
                    prev = nums[i]
                    continue

                elif nums[i] > prev:
                    return False

            return True
