
# verbose solution, 22.83ms 
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 2:
            return False

        stack = []

        for item in s:
            if item == '{':
                stack.append(item)
            elif item == '[':
                stack.append(item)
            elif item == '(':
                stack.append(item)

            if len(stack) >= 1:

                if item == '}':
                    latest = stack.pop()

                    if latest != '{':
                        return False

                elif item == ')':

                    latest = stack.pop()

                    if latest != '(':
                        return False

                elif item == ']':

                    latest = stack.pop()

                    if latest != '[':
                        return False

            elif len(stack) == 0:
                if item == '}' or item == ')' or item == ']' :
                    return False


        if len(stack) > 0:
            return False
        else:
            return True
        
        
# better
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in mapping.values():
                stack.append(char)
            elif char in mapping:
                if not stack or stack.pop() != mapping[char]:
                    return False
            else:
                return False

        return not stack