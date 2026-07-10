class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        # ans=[]
        # for i in range(len(temperatures)):
        #     flag=True
        #     for j in range(i+1,len(temperatures)):
        #         if temperatures[j]>temperatures[i]:
        #             flag=False
        #             ans.append(j-i)
        #             break
        #     if flag:
        #         ans.append(0)
        # return ans

        n=len(temperatures)
        ans=[0]*n
        st=[]
        for i in range(n):
            while st and temperatures[i]>st[-1][0]:
                temp,idx=st.pop()
                ans[idx]=i-idx
            st.append((temperatures[i],i))  
        return ans 
if __name__=='__main__':
    sol=Solution()
    print(sol.dailyTemperatures([73,74,75,71,69,72,76,73]))
    print(sol.dailyTemperatures([30,40,50,60]))
    print(sol.dailyTemperatures([30,60,90]))