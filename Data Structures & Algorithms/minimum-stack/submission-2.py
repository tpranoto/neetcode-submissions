class MinStack:

    def __init__(self):
        self.stack = []
        self.min_val = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.min_val) == 0:
            self.min_val.append(val)
            return
        
        if self.min_val[-1] >= val:
            self.min_val.append(val)

    def pop(self) -> None:
        cur = self.stack.pop()
        if self.min_val[-1] == cur:
            self.min_val.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_val[-1]
