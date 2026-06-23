from collections import defaultdict
import random
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # res=defaultdict(int)
        # for i in nums:
        #     res[i]+=1
        # print(res)
        # for key,val in res.items():
        #     if val>len(nums)//2:
        #         return key
        # return 0

        # n=len(nums)
        # bit=[0]*32

        # for num in nums:
        #     for i in range(32):
        #         bit[i]+=((num>>i)&1)
        # res=0
        # for i in range(32):
        #     if bit[i]>n//2:
        #         if i==31:
        #             res-=(1<<i)
        #         else:
        #             res |= (1<<i)
        # return res

        # res=cnt=0
        # for num in nums:
        #     if cnt==0:
        #         res=num
        #     cnt+=(1 if num==res else -1)
        # return res

        n=len(nums)
        while True:
            candt=random.choice(nums)
            if nums.count(candt)>n//2:
                return candt
   
if __name__=='__main__':
    sol=Solution()
    nums=[3,2,2,3,3]
    print(sol.majorityElement(nums))