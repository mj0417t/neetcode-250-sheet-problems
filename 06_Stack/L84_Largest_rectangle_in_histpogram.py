class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        # maxHt=0
        # for i in range(len(heights)):
        #     recHeight=heights[i]
        #     l,r=i-1,i+1
        #     while l>=0:
        #         if heights[l]<recHeight:
        #             break
        #         l-=1
        #     while r<len(heights):
        #         if heights[r]<recHeight:
        #             break
        #         r+=1
        #     #l and r stops at first smaller bar on each side
        #     # so rectangele spans from l+1 to r-1 
        #     maxHt=max(maxHt,recHeight*(r-l-1))
        # return maxHt

        # n=len(heights)
        # left=[-1]*n
        # st=[]
        # for i in range(n):
        #     while st and heights[st[-1]]>=heights[i]:
        #         st.pop()
        #     if st:
        #         left[i]=st[-1]
        #     st.append(i)
        
        # right=[n]*n
        # st=[]
        # for i in range(n-1,-1,-1):
        #     while st and heights[st[-1]]>=heights[i]:
        #         st.pop()
        #     if st:
        #         right[i]=st[-1]
        #     st.append(i)
        
        # maxHt=0
        # for i in range(n):
        #     maxHt=max(maxHt,heights[i]*(right[i]-left[i]+1))
        # return maxHt

        # st=[]
        # maxArea=0
        # for i,h in enumerate(heights):
        #     start=i
        #     while st and st[-1][1]>h:
        #         idx, ht=st.pop()
        #         maxArea=max(maxArea,ht*(i-idx))
        #         start=idx
        #     st.append((start,h))

        # for i,h in st:
        #     maxArea=max(maxArea,h*(len(heights)-i))
        # return maxArea


        st=[]
        maxArea=0
        n=len(heights)

        for i in range(n+1):
            while st and (i==n or heights[st[-1]]>=heights[i]):
                ht=heights[st.pop()]
                width = i if not st else i-st[-1]-1
                maxArea=max(maxArea, ht*width)
            st.append(i)
        return maxArea

if __name__=='__main__':
    sol=Solution()
    print(sol.largestRectangleArea([2,1,5,6,2,3]))
    print(sol.largestRectangleArea([2,4]))