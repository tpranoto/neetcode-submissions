class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        output=[]
        subset = []

        def dfs(i):
            cur_tot = sum(subset)
            if cur_tot == target:
                output.append(subset.copy())
                return
            if cur_tot > target or i >= len(nums):
                return
            
            subset.append(nums[i])
            dfs(i)
            subset.pop()
            dfs(i+1)
        
        dfs(0)

        return output
