class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)

        pref = 1

        for i in range(len(nums)):
            result[i] = pref
            pref *=nums[i]

        suf = 1

        for i in range(len(nums)-1,-1,-1):
            result[i] *=suf
            suf *= nums[i]
        
        return result