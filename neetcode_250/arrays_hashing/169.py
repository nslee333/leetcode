




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