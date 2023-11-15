# fastest so far
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        for item in nums:
            ans.append(item)
        for item in nums:
            ans.append(item)
        return ans


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(2):
            for item in nums:
                ans.append(item)
        return ans
