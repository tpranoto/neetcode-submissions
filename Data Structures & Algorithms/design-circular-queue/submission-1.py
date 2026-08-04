class MyCircularQueue:
    def __init__(self, size):
        self.size = size
        self.buffer = []

    def Front(self):
        if len(self.buffer) == 0:
            return -1

        return self.buffer[0]

    def Rear(self):
        if len(self.buffer) == 0:
            return -1

        return self.buffer[-1]

    def enQueue(self, value):
        if len(self.buffer) == self.size:
            return False

        self.buffer.append(value)
        return True

    def deQueue(self):
        if len(self.buffer) == 0:
            return False

        self.buffer.pop(0)
        return True

    def isEmpty(self):
        return len(self.buffer) == 0

    def isFull(self):
        return len(self.buffer) == self.size
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()