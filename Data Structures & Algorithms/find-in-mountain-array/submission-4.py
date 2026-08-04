class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        length = mountainArr.length()
        if length == 0:
            return -1

        l,r = 1, length-2
        m = (r+l) // 2
        while l<r:
            prev = mountainArr.get(m-1)
            cur = mountainArr.get(m)
            nxt = mountainArr.get(m+1)

            if prev < cur < nxt:
                l= m+1
            elif prev > cur > nxt:
                r= m-1
            else:
                break
            m = (r+l) // 2

        result = self.bs(target,0,m-1,mountainArr,True)     
        if  result != -1:
            return result

        return self.bs(target,m,length-1,mountainArr,False) 


    def bs(self, target, l,r, mountainArr,asc:bool):
        while l <= r:
            m = int((r+l) /2)
            midval = mountainArr.get(m)
            if target < midval:
                if asc:
                    r = m-1
                else:
                    l = m+1
            elif target > midval:
                if asc:
                    l = m+1
                else:
                    r = m-1
            else:
                return m

        return -1
