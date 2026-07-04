class Solution:
    def decrypt(self, code: list[int], k: int) -> list[int]:
        # n=len(code)
        # res=[0]*n
        # if k==0:
        #     return res
        # elif k>0:
        #     for i in range(n):
        #         for j in range(i+1,i+k+1):
        #             res[i]+=code[j%n]
        #     return res
        # else:
        #     for i in range(n):
        #         for j in range(i-1,i-1+k,-1):
        #             res[i]+=code[j]
        #     return res

        #using sliding window
        n=len(code)
        res=[0]*n
        if k==0:
            return res
        if k>0:
            res[0]=sum(code[1:k+1])
            for i in range(1,n):
                res[i]=res[i-1]-code[i]+code[(i+k)%n]
            return res
        else:
            res[0]=sum(code[k:])
            for i in range(1,n):
                res[i]=res[i-1]-code[(i+k-1)%n]+code[(i-1)%n]
            return res
        

if __name__=='__main__':
    sol=Solution()
    code1 = [5,7,1,4]
    k1= 3
    code2 = [1,2,3,4]
    k2 = 0
    code3 = [2,4,9,3]
    k3 = -2
    print(sol.decrypt(code1,k1))
    print(sol.decrypt(code2,k2))
    print(sol.decrypt(code3,k3))