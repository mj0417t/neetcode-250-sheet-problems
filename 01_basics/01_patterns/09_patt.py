#     *
#    ***
#   *****
#  *******
# *********
# *********
#  *******
#   *****
#    ***
#     *

class Solution:
    def pattern(self,n):
        for i in range(n):
            j=0
            while j<2*n:
                if j>=n-1-i and j<=n-1+i:
                    print('*',end='')
                else:
                    print(" ",end='')
                j+=1
            print()
        for i in range(n,0,-1):
            for j in range(n+i-1):
                if j<n-i:
                    print(" ", end='')
                else:
                    print('*',end='')
            print()



if __name__=='__main__':
    sol=Solution()
    n=5
    sol.pattern(5)