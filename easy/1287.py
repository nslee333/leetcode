class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        dict = {}
        for item in arr:
            if item in dict:
                dict[item] = dict.get(item) + 1
            else:
                dict[item] = 1
        
        k = 0
        k_count = 0
        for key, value in dict.items():
            if k_count == 0 or k_count < value:
                k_count = value
                k = key
           
        return k
