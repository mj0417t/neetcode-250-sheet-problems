from collections import defaultdict

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        # nums=sorted(nums)
        # print(nums)
        # max_lcs=curr_lcs=1
        # for i in range(1,len(nums)):
        #     if nums[i]==nums[i-1]:
        #         continue
        #     if nums[i]==nums[i-1]+1:
        #         curr_lcs+=1
        #     else:
        #         max_lcs=max(max_lcs,curr_lcs)
        #         curr_lcs=1
        # return max(max_lcs,curr_lcs)

        # numSet=set(nums)
        # longest=0
        # for num in numSet:
        #     if (num-1) not in numSet:
        #         length=1
        #         while (num +length) in numSet:
        #             length+=1
        #         longest=max(length,longest)
        # return longest

        mp=defaultdict(int)
        res=0
        for num in nums:
            if not mp[num]:
                mp[num]=mp[num-1]+mp[num+1]+1
                mp[num-mp[num-1]]=mp[num]
                mp[num+mp[num+1]]=mp[num]
                res=max(res,mp[num])

        return res

if __name__=='__main__':
    sol = Solution()
    nums1 = [100,4,200,1,3,2]
    nums2 = [0,3,7,2,5,8,4,6,0,1]
    nums3 = [1,2,6,7,8]
    print(sol.longestConsecutive(nums1))
    print(sol.longestConsecutive(nums2))
    print(sol.longestConsecutive(nums3))
    