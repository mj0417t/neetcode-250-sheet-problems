class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        # map={}
        # for num in nums:
        #     map[num]=1+map.get(num,0)
        # i=0
        # for key in map.keys():
        #     nums[i]=key
        #     i+=1
        # return i

        i=0
        j=1
        while j<len(nums):
            if nums[i]!=nums[j]:
                i+=1
                nums[i]=nums[j]
            j+=1
        
        return i+1


if __name__=='__main__':
    nums = [1,1,2]
    sol=Solution()
    ans=sol.removeDuplicates(nums)
    print(ans)
        