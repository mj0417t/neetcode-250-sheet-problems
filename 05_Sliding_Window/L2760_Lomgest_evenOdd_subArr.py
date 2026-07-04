class Solution:
    def longestAlternatingSubarray(self, nums: list[int], threshold: int) -> int:
        # maxls=0
        # n=len(nums)
        # for i in range(n):
        #     if nums[i]>threshold or nums[i]%2!=0:
        #         continue
        #     lens=1
        #     for j in range(i+1, n):
        #         if nums[j]> threshold or nums[j-1]%2==nums[j]%2:
        #             break
        #         lens+=1
        #     maxls=max(maxls,lens)
        # return maxls

        
        ans=i=0
        n=len(nums)

        while i<n:
            if nums[i]>threshold or nums[i]%2!=0:
                i+=1
                continue
            j=i
            while(j+1<n and nums[j+1]<=threshold
              and nums[j]%2!=nums[j+1]%2):
                j+=1
            ans=max(ans,j-i+1)
            i=j+1
        return ans

        
if __name__=='__main__':
    nums = [3,2,5,4]
    threshold = 5
    nums2 = [1,2]
    threshold2= 2
    nums3 = [2,3,4,5]
    threshold3 = 4
    sol=Solution()
    print(sol.longestAlternatingSubarray(nums,threshold))
    print(sol.longestAlternatingSubarray(nums2,threshold2))
    print(sol.longestAlternatingSubarray(nums3,threshold3))