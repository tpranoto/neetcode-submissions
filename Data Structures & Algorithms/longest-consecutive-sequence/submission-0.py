from collections import defaultdict
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        cons_map= defaultdict(int)
        result = 0

        for n in nums:
            if not cons_map[n]:
                left_len = cons_map[n-1]
                right_len = cons_map[n+1]
                current = 1 +left_len+right_len

                cons_map[n-left_len] = current
                cons_map[n+right_len] = current
                cons_map[n] = current

                result = max(result, current)

        return result