# A
# BB
# CCC
# DDDD
# EEEEE

class Solution:
    def pattern(self, n):
        k=65
        for i in range(n):
            for j in range(i+1):
                print(chr(k), end="")    
            print()
            k+=1

if __name__=='__main__':
    sol=Solution()
    n=5
    sol.pattern(n)