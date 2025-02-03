
# neetcode solution
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        res = []

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue
                

            l, r = i+1, len(nums) - 1
            while l < r:
                guess = nums[i] + nums[l] + nums[r]

                if guess > 0:
                    r -= 1

                elif guess < 0:
                    l += 1

                elif guess == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1

                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res


# modified solution
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        seen = set()

        result = []

        i = 0
        for i, a in enumerate(nums):
            print(i)
            if i > 0 and a == nums[i - 1]:
                continue
                
            left, right = i+1, len(nums) - 1

            while left < right:
                if left > i+1 and nums[left] == nums[left - 1]:
                    left += 1
                    continue

                guess = nums[i] + nums[left] + nums[right]

                if guess == 0:
            
                    addition = [nums[i], nums[left], nums[right]]
                    result.append(addition)

                    left += 1

                    # keeps shifting the pointer left
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
                elif guess > 0:
                    right -= 1
                elif guess < 0:
                    left += 1

        return result




# 3sum
# my working code, it works but it's not super concise:)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        seen = set()

        result = []

        i = 0
        for i, a in enumerate(nums):
            print(i)
            if i > 0 and a == nums[i - 1]:
                continue
                
            left, right = i+1, len(nums) - 1

            while left < right:
                if left > i+1 and nums[left] == nums[left - 1]:
                    left += 1
                    continue

                guess = nums[i] + nums[left] + nums[right]

                if guess == 0:
            
                    addition = [nums[i], nums[left], nums[right]]
                    result.append(addition)

                    left += 1
                elif guess > 0:
                    right -= 1
                elif guess < 0:
                    left += 1

        return result