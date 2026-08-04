import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []

        heap = []

        i = 0
        while i < len(nums):
            heapq.heappush(heap,(-nums[i],i))
            if i>=k-1:
                while heap[0][1] <= i-k:
                    heapq.heappop(heap)
                output.append(-heap[0][0])
            i+=1
        return output