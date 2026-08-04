class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        output = []

        def helper(subset,possible):
            if len(subset) == len(nums):
                output.append(subset.copy())
                return

            for p in nums:
                if p in possible:
                    subset.append(p)
                    possible.remove(p)
                    helper(subset,possible)
                    possible.add(p)
                    subset.pop()

        helper([],set(nums))

        return output