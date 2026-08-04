class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l,r = 0, len(nums)-1

        while l<r:
            mid = (r+l) //2

            if nums[mid] == nums[mid+1]:
                if (r - (mid+1)) %2 == 0:
                    r = mid-1
                else:
                    l = mid+2
            
            elif nums[mid-1] == nums[mid]:
                if ((mid-1)-l) %2 == 0:
                    l = mid+1
                else:
                    r = mid-2
            else:
                return nums[mid]
        
        return nums[l]