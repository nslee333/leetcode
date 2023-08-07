class MinStack:

    def __init__(self):
        self.stack = []
        print(self.stack)

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        if self.stack:
            return self.stack.pop(-1)
        
    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        
    def getMin(self) -> int:
        if self.stack:
            count = self.stack[0]
            for item in self.stack:
                if item < count:
                    count = item
                else:
                    continue
            return count