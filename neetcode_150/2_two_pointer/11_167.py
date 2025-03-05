

# 5 MS
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        result = []


        i, j = 0, len(numbers) - 1

        # changing != to < 
        while i < j:
            guess = numbers[i] + numbers[j]

            if guess == target:
                result = [i+1, j+1]
                return result
            elif guess > target:
                j -= 1
            elif guess < target:
                i += 1

        return result
        









# acceptable solution, 55ms, o n time, 0 1 space
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        result = []


        i, j = 0, len(numbers) - 1=

        while i != j:
            print(i, j)
            guess = numbers[i] + numbers[j]
            print(guess)

            if guess > target:
                j -= 1
            elif guess < target:
                i += 1
            elif guess == target:
                result = [i+1, j+1]
                return result
        return result






# unefficient solution, O N^2
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # O n time
        # exactly 1 solution


        # two pointers, slow&fast, slow - target = guess, 
        # keep looking forward until we see guess, if above target, 


        result = []


        for i in range(len(numbers)):


            j = i+1
            while j < len(numbers):
                if (numbers[j] + numbers[i]) > target:
                    break
                if numbers[j] + numbers[i] == target:
                    result = [i+1, j+1]
                    return result
                j += 1
        return result
        