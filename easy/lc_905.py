class Solution:
  def sortArrayByParity(self, nums: List[int]) -> List[int]:
    res = []

    for i in range(len(nums)):
      if nums[i] % 2 == 0:
        res.insert(0, nums[i])
      elif nums[i] % 2 != 0:
        res.append(nums[i])
    return res














