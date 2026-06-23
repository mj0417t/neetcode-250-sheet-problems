class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # tmp=[]
        # for i in nums:
        #     if i!=val:
        #         tmp.append(i)
        # for i in range(len(tmp)):
        #     nums[i]=tmp[i]
        # return len(tmp)

        # k=0
        # for i in range(len(nums)):
        #     if nums[i]!=val:
        #         nums[k]=nums[i]
        #         k+=1
        # return k

        n=len(nums)
        i=0
        while i<n:
            if nums[i]==val:
                n-=1
                nums[i]=nums[n]
            else:
                i+=1
        return n
    
if __name__=='__main__':
    sol=Solution()
    nums=[3,2,2,3]
    val=3
    print(sol.removeElement(nums,val))