# from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # c1=Counter(nums)
        # return [x for x,y in c1.most_common(k)]

        #using minheap
        # cnt={}
        # for val in nums:
        #     cnt[val]=1+cnt.get(val,0)

        # heap=[]

        # for num in cnt.keys():
        #     heapq.heappush(heap,(cnt[num],num))
        #     if len(heap)>k:
        #         heapq.heappop(heap)

        # res=[]
        # for i in range(k):
        #     res.append(heapq.heappop(heap)[1])
        # return res
        

        #using bucket sort
        cnt={}
        for val in nums:
            cnt[val]=1+cnt.get(val,0)

        freq=[[] for _ in range(len(nums)+1)]

        for num,count in cnt.items():
            freq[count].append(num)
        
        res=[]

        for i in range(len(freq)-1,0,-1):
            for num in freq[i]:
                res.append(num)
                if len(res)==k:
                    return res

        