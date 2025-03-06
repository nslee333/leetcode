# concatenation of array

# linear time O(n + n) so O(n) and space is the same
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        
        ans = []
        count = 1
        while count <= 2:
            for item in nums:
                ans.append(item)
            count += 1

        return ans
    
    
# linear time & space
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums + nums
