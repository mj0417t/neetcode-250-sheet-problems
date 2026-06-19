class Solution:
    def isPalindrome(self,str):
        return self.helper(0,len(str)-1,str)
    def helper(self, startIndex, endIndex, arr):
        if startIndex>=endIndex:
            return True
        if arr[startIndex]!=arr[endIndex]:
            return False
        else:
            return self.helper(startIndex+1, endIndex-1,arr)


if __name__=='__main__':
    sol=Solution()
    str='ABCDCBA'

    print(sol.isPalindrome(str))
    print(sol.isPalindrome('Take u forward'))
    