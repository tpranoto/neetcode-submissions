import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1, max(piles)

        min_rate = 0

        while l<=r:
            rate = (l+r) //2

            hrs = self.calcHrs(piles,rate)

            if hrs <= h:
                r= rate-1
                min_rate = rate
            else:
                l =rate+1
        
        return min_rate
                

    def calcHrs(self, piles, rate):
        hrs = 0

        for p in piles:
            hrs += math.ceil(p/rate)
        
        return hrs