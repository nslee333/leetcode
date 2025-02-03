
# pretty good
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operands = {'+', '-', '/', '*'}

        for i in range(len(tokens)):
            if tokens[i] in operands:
                y = int(stack.pop())
                x = int(stack.pop())

                if tokens[i] == '+':
                    temp = x + y
                elif tokens[i] == '-':
                    temp = x - y 
                elif tokens[i] == '/':
                    temp = x / y
                elif tokens[i] == '*':
                    temp = x * y
                stack.append(temp)

            else:
                stack.append(tokens[i])
        return int(stack[-1])