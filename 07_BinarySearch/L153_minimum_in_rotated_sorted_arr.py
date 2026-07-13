class Solution:
    def findMin(self, nums: list[int]) -> int:

        # Using brute force
        # n=len(nums)
        # if n==1:
        #     return nums[0]
        # if n==2:
        #     return nums[0] if nums[0]<nums[1] else nums[1]
        # for i in range(1,n-1):
        #     if nums[i]<nums[i-1] and nums[i]<nums[i+1]:
        #         return nums[i]
        # if nums[0]<nums[1] and nums[0]<nums[n-1]:
        #     return nums[0]
        # else:
        #     return nums[n-1]

        l,r=0,len(nums)-1
        while l<r:
            m=(l+r)//2
            if nums[m]<nums[r]:
                r=m
            else:
                l=m+1
        return nums[l]


if __name__=='__main__':
    sol=Solution()
    print(sol.findMin(nums = [3,4,5,1,2]))
    print(sol.findMin(nums = [4,5,6,7,0,1,2]))
    print(sol.findMin(nums = [11,13,15,17]))