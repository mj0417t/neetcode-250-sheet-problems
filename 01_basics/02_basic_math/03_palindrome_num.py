class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        else:
            num_str=str(x)
            if num_str==num_str[::-1]:
                return True
            return False        

if __name__=='__main__':
    sol=Solution()
    num=-43
    print(sol.isPalindrome(num))
    print(sol.isPalindrome(23456))
    print(sol.isPalindrome(12321))