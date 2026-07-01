class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # cnt=0
        # for i in range(len(nums)):
        #     sum=0
        #     for j in range(i,len(nums)):
        #         sum+=nums[j]
        #         if sum==k:
        #             cnt+=1
        # return cnt

        res=0
        currSum=0
        prefixSums={0:1} #prefix sum is zero before the arr is traversed

        for num in nums:
            currSum+=num
            diff=currSum-k
            res+=prefixSums.get(diff,0)
            prefixSums[currSum]=1+prefixSums.get(currSum,0)
        return res
if __name__=='__main__':
    sol = Solution()
    nums = [1,-1,1,-1,1]
    k = 0
    print(sol.subarraySum(nums,k))