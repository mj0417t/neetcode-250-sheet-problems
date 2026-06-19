class Solution:
    def reverse(self,arr):
        self.helper(0,len(arr)-1,arr)
    def helper(self, startIndex, endIndex, arr):
        if startIndex>=endIndex:
            return
        else:
            temp=arr[startIndex]
            arr[startIndex]=arr[endIndex]
            arr[endIndex]=temp
            self.helper(startIndex+1, endIndex-1,arr)


if __name__=='__main__':
    sol=Solution()
    arr=[1,2,4,5]

    sol.reverse(arr)
    print(arr)