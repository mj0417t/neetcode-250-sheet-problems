class Solution:
    def productExceptSelf(self, nums: list[int]) -> List[int]:
        # res=[]
        # for i in range(len(nums)):
        #     prod=1
        #     for j in range(len(nums)):
        #         if i==j:
        #             continue
        #         prod*=nums[j]
        #     res.append(prod)
        # return res

        # #using div
        # cnt_zero=0
        # for val in nums:
        #     if val==0:
        #         cnt_zero+=1
        # if cnt_zero>1:
        #     return [0]*len(nums)
        # else:
        #     idx_zero=-1
        #     prod=1
        #     for i in range(len(nums)):
        #         if nums[i]==0:
        #             idx_zero=i 
        #         else:
        #             prod*=nums[i]
        #     if idx_zero==-1:
        #         return [(int)(prod/val) for val in nums]
        #     else:
        #         res=[]
        #         for i in range(len(nums)):
        #             if i==idx_zero:
        #                 res.append(int(prod))
        #             else:
        #                 res.append(0)
        #         return res
#using prefixProd and suffixProd
        # prod=1
        # prefProd=[]
        # n=len(nums)
        # for i in range(n):
        #     if i==0:
        #         prod=1
        #     else:
        #         prod*=nums[i-1]
        #     prefProd.append(prod)
        # sufProd=[0]*n
        # for i in range(n-1,-1,-1):
        #     if i==n-1:
        #         prod=1
        #     else:
        #         prod*=nums[i+1]
        #     sufProd[i]=prod
        
        # res=[]
        # for i in range(n):
        #     res.append(prefProd[i]*sufProd[i])
        # return res

        # n=len(arr)
        # pre=[0]*n
        # suff=[0]*n
        # res=[0]*n

        # pre[0]=suff[n-1]=1

        # for i in range(1,n):
        #     pre[i]=pre[i-1]*nums[i-1]

        # for i in range(n-2,-1,-1):
        #     suff[i]=suff[i+1]*nums[i+1]
        
        # for i in range(n):
        #     res[i]=pre[i]* suff[i]
        # return res

        # optimal

        n=len(nums)
        res=[1]*n
        prefix=1
        for i in range(n):
            res[i]=prefix
            prefix*=nums[i]
        postfix=1
        for i in range(n-1,-1,-1):
            res[i]*=postfix
            postfix*=nums[i]
        return res

if __name__=='__main__':
    # arr=[3, 0, 1, 4, 2]
    arr=[-1,1,0,-3,3]
    # arr=[1,2,3,4]
    obj=Solution()
    print(obj.productExceptSelf(arr))
