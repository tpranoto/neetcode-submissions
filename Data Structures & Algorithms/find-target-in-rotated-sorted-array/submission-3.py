class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l,r = 0, len(nums)-1

        while l<r:
            mid = (l+r)//2

            if nums[mid]<nums[r]:
                r = mid
            else:
                l = mid+1

        min_idx = l

        if target <= nums[-1]:
            l = min_idx
            r = len(nums)-1
        else:
            l = 0
            r = min_idx

        while l<=r:
            mid = (r+l)//2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid-1
            else:
                l = mid+1

        return -1