class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]+nums[j]==target:
        #             return[i,j]
        # return [-1,-1]

        complements: dict[int, int]={}
        for i in range(len(nums)):
            rem=target-nums[i]
            if rem in complements:
                return [i,complements[rem]]
            complements[nums[i]]=i
        return [-1,-1]

if __name__=='__main__':
    s=Solution()
    arr=[3,2,4]
    target=6
    print(s.twoSum(arr,target))
        
        