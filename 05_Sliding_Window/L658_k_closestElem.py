class Solution:
    def findClosestElements(self, arr: list[int], k: int, x: int) -> list[int]:
        # arr.sort(key=lambda num:(abs(num-x),num))
        # return sorted(arr[:k])


        # n=len(arr)
        # idx=0
        # for i in range(1,n):
        #     if abs(x-arr[idx])> abs(x-arr[i]):
        #         idx=i
        # res=[arr[idx]]
        # l,r=idx-1,idx+1
        
        # while len(res)<k:
        #     if l>=0 and r<n:
        #         if abs(arr[l]-x)<=abs(arr[r]-x):
        #             res.append(arr[l])
        #             l-=1
        #         else:
        #             res.append(arr[r])
        #             r+=1
        #     elif l>=0:
        #         res.append(arr[l])
        #         l-=1
        #     elif r<n:
        #         res.append(arr[r])
        #         r+=1
        # return sorted(res)

        # l,r=0,len(arr)-1
        # while r-l+1>k:
        #     if abs(x-arr[l])>abs(x-arr[r]):
        #         l+=1
        #     else:
        #         r-=1
        # return arr[l:r+1]

        l,r=0,len(arr)-k
        while l<r:
            mid=(l+r)//2
            if x-arr[mid]>arr[mid+k]-x:
                l=mid+1
            else:
                r=mid
        return arr[l:l+k]    

if __name__=='__main__':
    arr1 = [1,2,3,4,5]
    k1 = 4
    x1 = 3
    arr2 = [1,1,2,3,4,5]
    k2 = 4
    x2= -1

    sol=Solution()
    print(sol.findClosestElements(arr1,k1,x1))
    sol.findClosestElements(arr2,k2,x2)