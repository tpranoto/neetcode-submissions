class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return []

        nums.sort()
        result = []

        for i, a in enumerate(nums):
            if a > 0:
                break

            if i > 0 and a == nums[i - 1]:
                continue

            l = i+1
            r = len(nums)-1

            while l < r:
                sums = a + nums[l] + nums[r]
                if sums > 0:
                    r -= 1
                elif sums < 0:
                    l += 1
                else:
                    result.append([a,nums[l],nums[r]])
                    r -=1
                    l +=1

                    while l < r and nums[l] == nums[l-1]:
                        l +=1
        

        return result