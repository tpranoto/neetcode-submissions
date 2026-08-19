class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        passes = {}

        for i,n in enumerate(nums):
            diff = target-n
            if diff in passes:
                return [passes[diff],i]
            passes[n] = i
        
        return []