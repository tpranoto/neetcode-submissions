import random 

class Solution:

    def __init__(self, w: List[int]):
        self.w = w
        self.sum = sum(w)
        

    def pickIndex(self) -> int:
        randomized_thres = self.sum * random.random()
        cur_sum = 0
        
        for i in range(len(self.w)):
            cur_sum += self.w[i]
            if cur_sum >= randomized_thres:
                return i

        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()