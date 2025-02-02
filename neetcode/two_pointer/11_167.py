


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
        