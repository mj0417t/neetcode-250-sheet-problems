# *        *
# **      **
# ***    ***
# ****  ****
# **********
# ****  ****
# ***    ***
# **      **
# *        *

class Solution:
    def pattern(self, n):
        for i  in range(2*n-1):
            if i<n:
                stars=i+1
            else:
                stars =2*n-1-i
            space=2*(n-stars)
            print('*'*stars+' '*space+'*'*stars)



if __name__=='__main__':
    sol=Solution()
    n=5
    sol.pattern(n)