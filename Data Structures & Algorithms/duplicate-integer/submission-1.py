class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        appeared = set()

        for n in nums:
            if n in appeared:
                return True

            appeared.add(n)

        return False
        
        
        
        
        # has_appeared = set()

        # for num in nums:
        #     if num in has_appeared:
        #         return True
        #     has_appeared.add(num)

        # return False