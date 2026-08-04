import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for p in points:
            heapq.heappush(heap,(self.calc(p[0],p[1]),p))

        res = []
        while heap and len(res)<k:
            dist,p = heapq.heappop(heap)
            res.append(p)
        
        return res

    
    def calc(self,x1,y1):
        return math.sqrt((x1-0)**2 + (y1-0)**2)