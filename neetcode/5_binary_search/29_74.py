

# neetcode solution, O(log n + log m) space O(1)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        ROWS, COLS = len(matrix), len(matrix[0])

        top, bot = 0, ROWS - 1
        while top <= bot:
            row = (top + bot) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                break

        if not (top <= bot):
            return False
        row = (top + bot) // 2
        l, r = 0, COLS - 1
        while l <= r:
            m = (l + r) // 2
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True
        return False

# my solution with chatgpt helping me in finding bugs in it
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        def search(self, array: List[int]) -> (bool, str):
            left, right = 0, len(array) - 1

            split = (len(array) - 1) // 2
         
            while left <= right:
                split = left + (right - left) // 2
                
                if array[split] < target:
                    left = split + 1
                elif array[split] > target:
                    right = split - 1
                else:
                    return True, 'none'

            if left > len(array) // 2:
                return False, 'higher'
            else:
                return False, 'lower'
            
        if not matrix or not matrix[0]:
            return False

        l, r = 0, len(matrix) - 1
        
        while l <= r:
            
            split_m = l + (r - l) // 2
            result = search(self, matrix[split_m])

            if result[0] == True:
                return True
            elif result[0] == False and result[1] == 'higher':
                
                l = split_m + 1
            elif result[0] == False and result[1] == 'lower':
                r = split_m - 1

            
        return False


# so technically this flattening approach passes the test cases for leetcode with a O(n) time complexity

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