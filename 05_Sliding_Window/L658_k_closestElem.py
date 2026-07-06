class Solution:
    def findClosestElements(self, arr: list[int], k: int, x: int) -> List[int]:
        l=0
        r=len(arr)
        while l<r:
            mid=(l+r)//2
            if abs(arr[mid]-x)<

if __name__=='__main__':
    arr1 = [1,2,3,4,5]
    k1 = 4
    x1 = 3
    arr2 = [1,1,2,3,4,5]
    k2 = 4
    x2= -1

    sol=Solution()
    sol.findClosestElements(arr1,k1,x1)
    sol.findClosestElements(arr2,k2,x2)