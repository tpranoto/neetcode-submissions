class MinStack:

    def __init__(self):
        self.buffer = []
        self.min_val = []
        

    def push(self, val: int) -> None:
        self.buffer.append(val)
        if len(self.min_val) == 0:
            self.min_val.append(val)
        elif self.min_val and self.min_val[-1] >= val:
            self.min_val.append(val)        

    def pop(self) -> None:
        val = self.buffer.pop()
        if val == self.min_val[-1]:
            self.min_val.pop()

    def top(self) -> int:
        return self.buffer[-1]
        

    def getMin(self) -> int:
        return self.min_val[-1]
        