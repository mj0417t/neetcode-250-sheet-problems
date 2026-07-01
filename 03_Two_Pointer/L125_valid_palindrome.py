class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(filter(str.isalnum,s)).lower()
        if s==s[::-1]:
            return True
        return False

if __name__=='__main__':
    s = "A man, a plan, a canal: Panama"
    sol=Solution()
    print(sol.isPalindrome(s))