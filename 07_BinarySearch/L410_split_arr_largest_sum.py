class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        # def canSplit(largest):
        #     subarr=1
        #     currSum=0
        #     for num in nums:
        #         currSum+=num
        #         if currSum>largest:
        #             subarr+=1
        #             if subarr>k:
        #                 return False
        #             currSum=num
        #     return True
        # l=max(nums)
        # r=sum(nums)
        # res=r
        # while l<=r:
        #     mid=(l+r)//2
        #     if canSplit(mid):
        #         res=mid
        #         r=mid-1
        #     else:
        #         l=mid+1
        # return res

        n=len(nums)
        prefixSum=[0]*(n+1)
        for i in range(n):
            prefixSum[i+1]=prefixSum[i]+nums[i]

        def canSplit(largest):
            subarr=0
            i=0
            while i<n:
                l,r=i+1,n
                while l<=r:
                    m=(l+r)//2
                    if prefixSum[m]-prefixSum[i]<=largest:
                        l=m+1
                    else:
                        r=m-1
                subarr+=1
                i=r
                if subarr>k:
                    return False
            return True

        l=max(nums)
        r=sum(nums)
        res=r
        while l<=r:
            mid=(l+r)//2
            if canSplit(mid):
                res=mid
                r=mid-1
            else:
                l=mid+1
        return res
        
if __name__=='__main__':
    sol=Solution()
    print(sol.splitArray(nums = [7,2,5,10,8], k = 2))
    print(sol.splitArray(nums = [1,2,3,4,5], k = 2))