class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        # if len(nums)<=k:
        #     return sum(nums)/k
        # l=0
        # s=0
        # maxAvg=float('-inf')
        # for r in range(len(nums)):
        #     if r-l >=k:
        #         s-=nums[l]
        #         l+=1
        #     s+=nums[r]
        #     if r-l==k-1:
        #         maxAvg=max(maxAvg,s/k)
        # return maxAvg


        window_sum=sum(nums[:k])
        max_sum=window_sum
        for i in range(k,len(nums)):
            window_sum=window_sum-nums[i-k]+nums[i]
            max_sum=max(max_sum, window_sum)
        return max_sum/k
    
    
if __name__=='__main__':
    sol=Solution()
    nums = [1,12,-5,-6,50,3]
    k = 4
    # nums = [5] 
    # k = 1
    print(f"{sol.findMaxAverage(nums,k):.5f}")
    print("{:.5f}".format(sol.findMaxAverage(nums,k)))