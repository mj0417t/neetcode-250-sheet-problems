# ABCDE
# ABCD
# ABC
# AB
# A

class Solution:
    def pattern(self, n):
        
        for i in range(n,0,-1):
            k=65
            for j in range(i):
                print(chr(k), end="")
                k+=1
            print()

if __name__=='__main__':
    sol=Solution()
    n=5
    sol.pattern(n)