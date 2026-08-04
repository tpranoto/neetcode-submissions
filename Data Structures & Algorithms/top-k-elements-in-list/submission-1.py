import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countMap = {}
        for n in nums:
            if n in countMap:
                countMap[n] +=1
            else:
                countMap[n] = 0

        pq = []
        for key,count in countMap.items():
            heapq.heappush(pq,(-count,key))
        
        result = []
        for _ in range(k):
            count,key = heapq.heappop(pq)
            result.append(key)

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