class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        if sum(nums)<target:
            return 0
        minLen=100001
        l,total=0,0
        for r in range(len(nums)):
            total+=nums[r]
            while total>=target and l<len(nums):
                minLen=min(minLen,r-l+1)
                total-=nums[l]
                l+=1
        return minLen



if __name__=='__main__':
    target1 = 7
    nums1 = [2,3,1,2,4,3]
    target2 = 4
    nums2 = [1,4,4]
    target3 = 11
    nums3 = [1,1,1,1,1,1,1,1]
    sol=Solution()
    print(sol.minSubArrayLen(target1,nums1))
    print(sol.minSubArrayLen(target2,nums2))
    print(sol.minSubArrayLen(target3,nums3))