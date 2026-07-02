class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        
        # for i in range(len(nums)-2):
        #     for j in range(i+1,len(nums)-1):
        #         for k in range(j+1,len(nums)):
        #             if nums[i]+nums[j]+nums[k]==0:
        #                 temp=[nums[i],nums[j],nums[k]]
        #                 temp.sort()
        #                 if temp not in res:
        #                     res.append(temp)
        res=[]
        nums.sort()
        for i in range(len(nums)-2):
            if nums[i]>0:
                break
            if i>0 and nums[i]==nums[i-1]:
                continue
            j=i+1
            k=len(nums)-1

            while j<k:
                if nums[j]+nums[k]==-1*nums[i]:
                    res.append([nums[i],nums[j],nums[k]])
                    while j<k and nums[j]==nums[j+1]:
                        j+=1
                    while j<k and nums[k]==nums[k-1]:
                        k-=1
                    j+=1
                    k-=1                   

                elif nums[j]+nums[k]<-1*nums[i]:
                    j+=1
                else:
                    k-=1
        return res
if __name__=='__main__':
    nums = [-1,0,1,2,-1,-4]
    sol=Solution()
    ans=sol.threeSum(nums)
    print(ans)
        