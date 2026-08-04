import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_map = {}

        for n in nums:
            if n in count_map:
                count_map[n] += 1
            else:
                count_map[n] = 1

        buckets = [[] for i in range(len(nums)+1)]

        for key,count in count_map.items():
            buckets[count].append(key)

        result = []
        for i in range (len(buckets)-1,0,-1):
            for key in buckets[i]:
                result.append(key)
                if len(result) == k:
                    return result






        # num_counts = {}
        # for n in nums:
        #     if n not in num_counts:
        #         num_counts[n] = 1
        #     else:
        #         num_counts[n] += 1
        
        # freq_buffer = []

        # for key,val in num_counts.items():
        #     heapq.heappush(freq_buffer,(-(val),key))
        
        # result = []
        # for _ in range(k):
        #     result.append(heapq.heappop(freq_buffer)[1])

        # return result