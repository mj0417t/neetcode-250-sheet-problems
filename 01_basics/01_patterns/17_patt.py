#    A
#   ABA
#  ABCBA
# ABCDCBA

class Solution:
    def pattern(self, n):
        for i in range(n):
            k=65
            for j in range(2*n-1):
                if j>=n-1-i and j<=n-1+i:
                    print(chr(k), end="")  
                    if j<n-1:
                        k+=1 
                    else:
                        k-=1
                else:
                    print(" ",end='') 
                
            print()

if __name__=='__main__':
    sol=Solution()
    n=4
    sol.pattern(n)