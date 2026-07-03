class Solution:
    def trap(self, height: list[int]) -> int:
        # n=len(height)
        # leftMax=[0]*n
        # rightMax=[0]*n

        # leftMax[0]=height[0]
        # for i in range(1,n):
        #     if height[i]>leftMax[i-1]:
        #         leftMax[i]=height[i]
        #     else:
        #         leftMax[i]=leftMax[i-1]
        
        # rightMax[n-1]=height[n-1]
        # for i in range(n-2,-1,-1):
        #     if height[i]> rightMax[i+1]:
        #         rightMax[i]=height[i]
        #     else:
        #         rightMax[i]=rightMax[i+1]
        
        # water =0
        # for k  in range(n):
        #     water+= min(leftMax[k],rightMax[k])-height[k]
        # return water

        #using two pointer

        l=0
        r=len(height)-1
        water=0
        leftMax=height[l]
        rightMax=height[r]

        while l<r:
            if leftMax<=rightMax:
                l+=1
                leftMax=max(leftMax, height[l])
                water+=leftMax-height[l]
            else:
                r-=1
                rightMax=max(rightMax,height[r])
                water+=rightMax-height[r]
        return water
        

if __name__=='__main__':
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    sol=Solution()
    ans=sol.trap(height)
    print(ans)