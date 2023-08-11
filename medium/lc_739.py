class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_index = stack.pop()
                result[prev_index] = i - prev_index 
            stack.append(i)
        return result
    
# same concept but using enumerate, above is simpler.

# class Solution:
# def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
#     stack = []
#     result = [0] * len(temperatures)

#     for i, t in enumerate(temperatures):
#         while stack and t > stack[-1][0]:
#             stack_t, stack_i = stack.pop()
#             result[stack_i] = (i - stack_i)
#         stack.append([t, i])
#     return result