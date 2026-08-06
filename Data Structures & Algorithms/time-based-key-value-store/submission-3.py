class TimeMap:

    def __init__(self):
        self.kv={}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.kv:
            self.kv[key] = []
        
        self.kv[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.kv or len(self.kv[key])==0:
            return ""

        l,r=0,len(self.kv[key])-1
        res = ""
        while l<=r:
            mid = (l+r)//2

            if self.kv[key][mid][0]<=timestamp:
                l = mid+1
                res = self.kv[key][mid][1]
            else:
                r=mid-1
        return res

        
