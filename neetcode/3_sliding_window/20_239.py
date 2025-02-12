
# optimized leetcode happy solution...


# so this uses a monotonically decreasing stack, meaning that it goes
# [higher.... -> lower]

# it's similar to a stack, but we can pop off the front and the end.
# 

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        output = []
        q = collections.deque()
        l = r = 0

        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            if l > q[0]:
                q.popleft()
            
            if (r + 1) >= k:
                output.append(nums[q[0]])
                l += 1
            r += 1
           
        return output


# too slow for leetcode, so not technically a good solution
# I think this is an O N * K (window) time & O(N) space
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        window = {}

        for i in range(0, len(nums) - k+1):
            temp = float('-inf')
            
            for r in range(i, i + k):
                # print("temp: ",temp)
                # print("nums[r]:", nums[r])
                temp = max(temp, nums[r])
            res.append(temp)
        return res
