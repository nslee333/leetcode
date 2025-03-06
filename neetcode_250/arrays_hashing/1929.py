# concatenation of array

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        
        ans = []
        count = 1
        while count <= 2:
            for item in nums:
                ans.append(item)
            count += 1

        return ans
        
        
        
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        
        return nums + nums
