class TimeMap:

    def __init__(self):
        self.timeMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timeMap:
            self.timeMap[key] = []
        
        self.timeMap[key].append((value,timestamp))
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timeMap or len(self.timeMap[key])==0:
            return ""


        l,r = 0, len(self.timeMap[key])-1
        result = ""
        while l<=r:
            mid = (l+r)//2

            if timestamp < self.timeMap[key][mid][1]:
                r = mid-1
            elif timestamp >= self.timeMap[key][mid][1]:
                result = self.timeMap[key][mid][0]
                l = mid+1

        return result