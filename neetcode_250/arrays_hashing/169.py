


# neetcode boyer moore voting algorithm, linear time and constant space
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res, count = float('-inf'), 0

        for n in nums:
            if n == res:
                count += 1
            elif n != res and count == 0:
                res = n
                count = 1
            else: 
                count -= 1
        
        return res

# neetcode hash table soltution

# keep a steady count of element and count as you go, then return res

# faste
class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        table = {}

        res, max_count = 0, 0
    
        for n in nums:
            table[n] = 1 + table.get(n, 0)
            res = n if table[n] > max_count else res
            max_count = max(table[n], max_count)
        return res


# not optimal
# my solution, linear time O(n + m), n for number of nums, and m for interating over table
# linear space for table
class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        table = {}

        for item in nums:
            table[item] = 1 + table.get(item, 0)
        return max(table, key=table.get)
    
    
    
# without one-liner
class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        table = {}

        for item in nums:
            table[item] = 1 + table.get(item, 0)
            
            
        max_value = float('-inf')
        max_key = -1
        
        for key, value in table.items():
            if value > max_value:
                max_value = value
                max_key = key
        return max_key