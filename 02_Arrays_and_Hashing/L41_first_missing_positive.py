# from collections import Counter
class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        maxi=max(nums)
        # for i in range(1,maxi+1):
        #     if nums.count(i)==0:
        #         return i
        # if maxi<0:
        #     return 1
        # c1=Counter(nums)
        # for i in range(1,maxi+1):
        #     if c1[i]==0:
        #         return i
        # return maxi+1

        n=len(nums)
        print(n)
        for i in range(n):
            if nums[i]<0:
                nums[i]=0

        for num in nums:
            val=abs(num)
            if 1<=val<=n:
                if nums[val-1]>0:
                    nums[val-1]*=-1
                elif nums[val-1]==0:
                    nums[val-1]=-1*(n+1)
        
        for i in range(n):
            if nums[i]>0:
                return i+1
        return n+1

if __name__=='__main__':
    sol = Solution()
    nums = [98,93,95,10,91,4,90,88,56,84,65,62,83,80,78,60,73,77,76,29,63,12,57,17,69,68,50,11,31,33,8,42,38,7,0,37,48,26,20,44,46,43,52,51,47,18,49,58,2,39,30,81,22,55,36,40,15,27,21,32,64,41,53,19,28,24,9,25,3,59,66,82,61,70,23,34,71,54,74,-1,1,45,14,79,5,35,13,72,75,85,87,6,16,86,67,89,94,92,96,97]
    # nums = [3,4,-1,1]
    # nums = [1,2,0]
    print(sol.firstMissingPositive(nums))        