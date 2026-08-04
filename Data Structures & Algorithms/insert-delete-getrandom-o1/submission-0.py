import random

class RandomizedSet:

    def __init__(self):
        self.numMap = {}
        self.num = []

    def insert(self, val: int) -> bool:
        if val in self.numMap:
            return False
        self.num.append(val)
        index = len(self.num) - 1
        self.numMap[val] = index

        return True

    def remove(self, val: int) -> bool:
        if val not in self.numMap:
            return False
        rm_idx = self.numMap[val]
        if rm_idx != len(self.num) - 1:

            temp_val = self.num[rm_idx]
            self.num[rm_idx] = self.num[-1]
            self.numMap[self.num[-1]] = rm_idx
            self.num[-1] = temp_val
            self.numMap[temp_val] = len(self.num)-1
        
        del self.numMap[val]
        self.num.pop()

        return True

    def getRandom(self) -> int:
        return random.choice(self.num)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()