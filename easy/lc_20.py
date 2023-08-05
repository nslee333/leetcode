class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0:
            return False

        dict = {
            ')': '(',
            ']': '[',
            '}': '{',
        }

        stack = []
        s = [*s]

        for elem in s:
            if elem in dict.values():
                stack.append(elem)
            elif elem in dict.keys():
                if len(stack) == 0: return False

                prev = stack.pop()
                if dict.get(elem) == prev:
                    continue
                else:
                    return False
                
        if len(stack) == 0:
            return True
        else:
            return False