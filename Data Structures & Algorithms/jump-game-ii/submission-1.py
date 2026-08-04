class Solution:
    def jump(self, nums: List[int]) -> int:
        memo = {}

        def dfs(i):
            if i in memo:
                return memo[i]
            if i == len(nums)-1:
                return 0
            if nums[i] == 0:
                return 99999
            
            res = 99999
            
            end = min(len(nums),i+nums[i]+1)

            for x in range(i+1,end):
                res = min(res,1+dfs(x))

            memo[i] = res
            return res

        return dfs(0)