class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums)-1

        while l<r:
            mid = (l+r) //2

            if nums[mid]<nums[r]:
                r = mid
            else:
                l = mid+1
        
        if target > nums[-1]:
            r = l
            l = 0
        else:
            r=len(nums)-1
        
        while l<=r:
            mid = (l+r)//2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r=mid-1
            else:
                l=mid+1
        return -1
