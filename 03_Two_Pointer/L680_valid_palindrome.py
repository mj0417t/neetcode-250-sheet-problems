class Solution:
    def validPalindrome(self, s: str) -> bool:
        # def isPalindrome(l,r):
        #     while l<r:
        #         if s[l]!=s[r]:
        #             return False
        #         l+=1
        #         r-=1
        #     return True

        # l=0
        # r=len(s)-1
        # while l<r:
        #     if s[l]!=s[r]:
        #         return isPalindrome(l+1,r) or isPalindrome(l,r-1)
        #     l+=1
        #     r-=1
        # return True
        if s==s[::-1]:
            return True
        l=0
        r=len(s)-1
        while l<r:
            if s[l]!=s[r]:
                return s[l+1:r+1]==s[l+1:r+1][::-1] or s[l:r]==s[l:r][::-1]
            l+=1
            r-=1
        return True

if __name__=='__main__':
    s = "abca"
    s1="aba"
    s3="zryxeededexyz"
    s2="aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga"
    sol=Solution()
    print(sol.validPalindrome(s))
    print(sol.validPalindrome(s1))
    print(sol.validPalindrome(s3))
    print(sol.validPalindrome(s2))