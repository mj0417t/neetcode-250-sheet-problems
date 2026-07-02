class Solution:
    def maxArea(self, height: list[int]) -> int:
        # maxAmt=0
        # for i in range(len(height)-1):
        #     for j in range(i+1,len(height)):
        #         amt=min(height[i],height[j])*(j-i)
        #         maxAmt=max(maxAmt,amt)
        # return maxAmt

        l,r=0,len(height)-1
        maxAmt=0
        while l<r:
            amt=min(height[l],height[r])*(r-l)
            maxAmt=max(maxAmt,amt)
            if height[l]<=height[r]:
                l+=1
            else:
                r-=1
        return maxAmt

if __name__=='__main__':
    height = [1,8,6,2,5,4,8,3,7]
    sol=Solution()
    ans=sol.maxArea(height)
    print(ans)