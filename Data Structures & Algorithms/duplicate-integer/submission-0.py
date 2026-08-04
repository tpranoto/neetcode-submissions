class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        has_appeared = set()

        for num in nums:
            if num in has_appeared:
                return True
            has_appeared.add(num)

        return False