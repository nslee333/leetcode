
# so technically this passes the test cases for leetcode, 

# but it demands a log(n * m) time complexity solution, so technially this doesn't count
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        temp = []

        for array in matrix:
            for item in array:
                temp.append(item)
        
        l, r = 0, len(temp) - 1

        split = len(temp) // 2

        while l <= r:
            split = l + (r - l) // 2
            
            if temp[split] < target:
                l = split + 1
            elif temp[split] > target:
                r = split - 1
            else:
                return True
        return False
        