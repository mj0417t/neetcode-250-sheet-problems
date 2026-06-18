# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *

class Solution:
    def pattern(self,n):
        for i in range(n):
            for j in range(i+1):
                print('*', end='')
            print()
        for i in range(n,0,-1):
            for j in range(i-1):
                print('*', end='')
            print()



if __name__=='__main__':
    sol=Solution()
    n=5
    sol.pattern(n)