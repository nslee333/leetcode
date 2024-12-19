
# Brute force, super slow O of N^2
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # brute force first

        # [2,7,11,15]
            # 0, 1 -> 0,2 -> 

        # loop 1:
            # loop 2:
                # if i == j
                    # continue
                # elif elem + elem == target
                    # return [i,j]
        
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    continue
                elif (nums[i] + nums[j]) == target:
                    return [i, j]

# Hash Table, 2 pass -> O of N,
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # hash_table = value => [index, i...]
        hash_table = {}

        # loop 1
            # if hash_table.get(item) != None:
                # hashtable[item].append(item)
            # else
                # hash_table[item] = [index]
        
        for i in range(len(nums)):
            item = nums[i]
            if hash_table.get(item) != None:
                hash_table[item].append(i)
            else:
                hash_table[item] = [i]

        # loop 2
            # value = target - item
            # position = hash_table.get(value)
            # if position != None:
                # return [j, position]

        for j in range(len(nums)):
            item = nums[j]
            other_value = target - item
            position = hash_table.get(other_value)
            if position != None:
                if position[0] == j:
                    continue
                return [position[0], j]
