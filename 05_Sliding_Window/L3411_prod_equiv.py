import math
class Solution:
    def maxLength(self, nums: list[int]) -> int:
        # lens=0
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if math.prod(nums[i:j+1])==reduce(math.lcm,nums[i:j+1])*reduce(math.gcd,nums[i:j+1]):
        #             lens=max(lens,j-i+1)
        # return lens

        ans=1
        for i in range(len(nums)):
            prod,l,g=1,1,0
            for j in range(i, len(nums)):
                prod*=nums[j]
                l=math.lcm(l,nums[j])
                g=math.gcd(g,nums[j])
                if prod==l*g:
                    ans=max(ans,j-i+1)
        return ans

if __name__=='__main__':
    nums = [1,2,1,2,1,1,1]
    nums2 = [2,3,4,5,6]
    nums3 = [1,2,3,1,4,5,1]
    sol=Solution()
    print(sol.maxLength(nums))
    print(sol.maxLength(nums2))
    print(sol.maxLength(nums3))