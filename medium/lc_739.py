class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        # return an array answer such that answer[i] is the # of days you have to wait for a warmer temp
        stack = []
        result = []

        for i in range(len(temperatures)-1):

            print(temperatures[i])
            j = i + 1
            
            
            if i == len(temperatures)-1:
                result.append(0)

            if j < len(temperatures)-1:
                while temperatures[j] <= temperatures[i]:
                    stack.append(temperatures[i])
                    j += 1

            if j > len(temperatures)-1 and len(stack) == 0:
                result.append(0)
                continue


            if temperatures[j] > temperatures[i]:
                stack.append(temperatures[i])
                result.append(len(stack))
                stack.clear()
                continue
        return result



        

# Of course, I'd be happy to help you with your code for the LeetCode problem 739. You're on the right track, but there are a few issues in your code that I'd like to point out and suggest improvements for.

# Loop Range:
# In your loop, you're using for i in range(len(temperatures)), which includes the last element. However, you're comparing temperatures[j] with temperatures[i] where j starts as i + 1, which means you might end up comparing an out-of-bounds index. To fix this, you should loop up to len(temperatures) - 1 to avoid going out of bounds.

# Condition for Appending to Result:
# The condition you're using to append the waiting days to the result list is not accurate. You need to calculate the difference between the current index and the index of the warmer day, rather than just appending the length of the stack. Also, you need to pop elements from the stack until you find a warmer temperature.

# Loop Condition:
# The loop condition while temperatures[j] <= temperatures[i] inside the inner loop is problematic. It doesn't guarantee that you'll find the next warmer day correctly. You should compare the temperatures between the current day and all future days until you find a warmer one.

# Stack Handling:
# You're using a stack to store temperatures, but your handling of the stack isn't quite correct. You don't need to clear the stack every time you find a warmer day. You can simply pop elements from the stack until you find a temperature higher than the current day's temperature.

# Logic for Handling Last Element:
# Your logic for handling the last element of the temperatures array is causing issues. You're comparing j > len(temperatures) - 1 which is not correct. You should compare j == len(temperatures) and then check if the stack is empty to determine whether to append 0 to the result.

# Here's an improved version of your code:
